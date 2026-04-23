num_of_steps = 3
template = """We made {total_observations} observations by tossing a coin: {tails_count} were tails and {heads_count} were heads.
The probabilities are {tails_probability:.2f}% and {heads_probability:.2f}%, respectively.
Our forecast is that the next {forecast_steps} observations will be: {tails_predict_full} and {heads_predict_full}."""