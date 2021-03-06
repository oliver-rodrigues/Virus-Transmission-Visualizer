import configparser

config = configparser.ConfigParser()
config['SARS-COV-1'] = {
        "type": "SARS-COV-1",
        "local_distance": 5,
        "long_distance": 15,
        "infection_distance": 3,
        "infection_duration": 480,
        "mask_prob_infected_out_range": 0.2,
        "mask_prob_infected_in_range": 0.5,
        "mask_prob_susceptible": 0.5,
        "mask_prob_both_out_range": 0.02,
        "mask_prob_both_in_range": 0.25,
        "time_conversion_factor": 24,
        "base_infection_probability": 0.3,
        "daily_prob_change": 0.9,
        "peak_infection_sars": 12,
        "daily_prob_increase_sars": 1.05,
        "daily_prob_decrease_sars": 0.95,
        "asymptomatic_probability": 0.3,
        "testing_probability": 0.5,
        "contact_tracing_efficiency": 0.75,
        "community_travel_probability": 0.08,
        "visit_hub_probability": 0.05,
        "asymptotic_testing_probability": 0.5,
        "quarantine_probability": 0.25,
        "incubation_period": 4
}
config['SARS-COV-2'] = {
        "type": "SARS-COV-2",
        "local_distance": 5,
        "long_distance": 15,
        "infection_distance": 7,
        "infection_duration": 480,
        "mask_prob_infected_out_range": 0.2,
        "mask_prob_infected_in_range": 0.5,
        "mask_prob_susceptible": 0.5,
        "mask_prob_both_out_range": 0.02,
        "mask_prob_both_in_range": 0.25,
        "time_conversion_factor": 24,
        "base_infection_probability": 0.19,
        "daily_prob_change": 0.95,
        "asymptomatic_probability": 0.3,
        "testing_probability": 0.5,
        "contact_tracing_efficiency": 0.5,
        "community_travel_probability": 0.05,
        "visit_hub_probability": 0.1,
        "asymptotic_testing_probability": 0.3,
        "quarantine_probability": 0.1,
        "incubation_period": 7

}

with open('dev.ini', 'w') as f:
    config.write(f)