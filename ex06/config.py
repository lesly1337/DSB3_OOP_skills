num_of_steps = 3
template = """We made {total_observations} observations by tossing a coin: {tails_count} were tails and {heads_count} were heads.
The probabilities are {tails_probability:.2f}% and {heads_probability:.2f}%, respectively.
Our forecast is that the next {forecast_steps} observations will be: {tails_predict_full} and {heads_predict_full}."""
BOT_TOKEN = "8283085827:AAFKIiacIMu5k3p2fse5k22FlDan1C-PVFI"
CHAT_ID = 958754235
API_url = f"https://api.telegram.org/bot{BOT_TOKEN}"