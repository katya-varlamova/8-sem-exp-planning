import math
from distributions import *
from queuing_system import *

def modelling(clients_number, lambda_coming, lambda_obr):
    params_generator = [1 / lambda_coming, 1]
    params_handler = [1 / lambda_obr, 1]
    print(params_generator, params_handler)
    source_generator1 = Generator(gauss_t, params_generator)
    handler_generator1 = Handler(gauss_t, params_handler)
    gov = ModelingGoverner(clients_number, [source_generator1], [handler_generator1], 0)
    s = gov.event()
    reqs = s.getRequests()
    n = 0  
    last_creation = 0
    t_creation = 0
    t_in = 0
    t_handling = 0
    n_handled = 0
    time = s.getMaxTime()
    for r in reqs:
        if r.getHandlingTime() > 0:
            t_creation += r.getCreationTime() - last_creation
            n += 1
            t_in += r.getStartHandlingTime() + r.getHandlingTime() - r.getCreationTime()

##            if r.getStartHandlingTime() + r.getHandlingTime() < time:
            n_handled += 1
            t_handling += r.getHandlingTime()
##        else:
##            t_in += time - r.getCreationTime()
        last_creation = r.getCreationTime()
            

    if n_handled > 0:
        t_in /= n_handled
    if n > 0:
        t_creation /= n
    if n_handled > 0:
        t_handling /= n_handled
    result = {"wait_time_middle" : t_in, "creation_time_middle" : t_creation,
              "handling_time_middle" : t_handling}
    print("Загрузка системы(расчетная): ", lambda_coming/lambda_obr, 
    "\nСреднее время пребывания: ", result['wait_time_middle'])
    return result
