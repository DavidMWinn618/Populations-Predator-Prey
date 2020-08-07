# Get numpy because we are using numpy.floor, and numpy.ceil

import numpy as np


# define prey as a population with carrying capacity, fertility, and mortality... don't worry about how much they eat, that's in fertility.

prey_pop = 109      # population of prey
prey_cap = 100000   # carrying capacity of environment of prey 
prey_frt = 0.05     # fertility rate of prey  
prey_mrt = 0.03     # mortality rate of prey ( natural causes ) 

pred_pop = 8        # predator population 
pred_cap = 1000     # carrying capacity of predator environment   
pred_frt = 0.05     # fertility rate of predator
pred_mrt = 0.03     # mortality rate of prey ( natural causes )

pred_vor = 1        # voracity of predator ( how much eaten per generation )


def prey_births( pop, cap, frt ):    
    return( np.floor( ( pop * frt ) * ( 1 - ( pop / cap ) ) ) )

def prey_deaths( pop, mrt ):    
    return( np.ceil( ( pop * mrt ) ) )

def eaten( prd_pop, pry_pop, prd_vor, prd_cap ):               # <=========== this needs fixed.
    return( prd_pop - pry_pop * ( 1 - ( pop / prd_cap ) ) )





def pred_births( pop, cap, frt, pry_pop ):                       # <=========== this needs fixed.
    return( np.floor( ( pop * frt ) * ( 1 - ( pop / cap ) ) ) )



eat_mod = eaten( pred_pop, prey_pop, pred_vor, pred_cap )            # <=========== this needs fixed.

def pred_deaths( pop, mrt, eat_mod ):    
    return( np.ceil( ( pop * mrt ) ) )



prey_pop_nxt = prey_pop + prey_births( prey_pop, prey_cap, prey_frt ) - prey_deaths( prey_pop, prey_mrt ) - eaten( pred_pop, prey_pop, pred_cap )

pred_pop_nxt = pred_pop + pred_births( pred_pop, pred_cap, pred_frt, prey_pop ) - pred_deaths( pred_pop, pred_mrt, eat_mod )




print( prey_pop )





