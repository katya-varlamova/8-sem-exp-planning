#pragma once

#include <array>
#include <cassert>
#include <cmath>
#include <tuple>
#include <vector>

#include "combinatorics.hpp"
std::vector<std::vector<int>> CreateUnitPlanningMatrix(size_t k);
std::vector<std::vector<int>> CreateUnitPlanningMatrix2();
std::vector<std::vector<double>> ToDouble(const std::vector<std::vector<int>> &m);

std::vector<std::vector<double>> Transpose(const std::vector<std::vector<double>> &m);

std::vector<std::vector<double>> MultMatrix(const std::vector<std::vector<double>> &l, const std::vector<std::vector<double>> &r);

struct Range {
	double min;
	double max;
	bool last;

	double Choose(bool c) {
	    last = c;
		return c ? max : min;
	}

	double Norm(double x) {
        if (abs(min - max) < 0.01)
            return last ? 1.0 : -1.0;
		return 2.0 * (x - min) / (max - min) - 1.0;
	}
};


struct FfeParameters {
	Range lambda1;
	Range lambda2;
	Range mu1;
	Range mu2;
	Range sigma_lambda1;
	Range sigma_lambda2;
	size_t times;
};

struct FfeTableRow {
	size_t index;
	double x1;
	double x2;
	double x3;
	double x4;
	double x5;
	double x6;
	double y_mean;
	double y_var;
	double y_hat;
	double dy_hat;
	double u_hat;
	double du_hat;
};

template <size_t k>
class PartialNonlinearCoefficients {
public:
	PartialNonlinearCoefficients()
		: N_(std::pow(2u, k))
		, a_(N_)
	{
		static_assert(1 <= k && k <= 6, "1 <= k <= 6");
	}

	size_t N() const {
		return N_;
	}

	double& operator[](size_t i) {
		return a_.at(i);
	}

	double operator[](size_t i) const {
		return a_.at(i);
	}

	template <typename... Args, typename = std::enable_if_t<std::conjunction_v<std::is_convertible<Args, size_t>...>>>
	double a(Args... indices) const {
		constexpr size_t size = sizeof...(indices);
		static_assert(size <= k, "size > k");

		const std::array<size_t, size> indices_array{{static_cast<size_t>(indices)...}};

		const size_t index = CalculateIndexStartOf(size) + CalculateIndexOfCombination(k, indices_array) - 1;

		return a_[index];
	}

	static constexpr size_t CalculateIndexStartOf(size_t together) {
		return together ? CalculateIndexStartOf(together - 1) + CalculateBinomialCoefficient(k, together - 1) : 0;
	}

private:
	size_t N_;
	std::vector<double> a_;
};

using FfeTable = std::vector<FfeTableRow>;

struct FfeResult {
	FfeTable table;
	PartialNonlinearCoefficients<6> coefficients;
};

struct DotParameters {
	double lambda1;
	double lambda2;
	double mu1;
	double mu2;
	double sigma_lambda1;
	double sigma_lambda2;
};

FfeResult FullFactorialExperiment(FfeParameters params);
FfeResult FractionalFactorialExperiment(FfeParameters params);

std::vector<double> NormalizeFactors(FfeParameters ffe_params, const DotParameters& dot_params);
double CalculateDotWithRegression(const PartialNonlinearCoefficients<6>& coefficients, const std::vector<double>& factors, size_t limit);
double CalculateDot(const DotParameters& dot_params, size_t times);
