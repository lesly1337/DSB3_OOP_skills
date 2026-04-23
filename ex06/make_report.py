import sys
from analytics import Research, Analytics
import config
if __name__ == '__main__':
    research = Research(sys.argv[1])
    if (len(sys.argv) == 2):
        list_of_lines = research.file_reader()
        calc = research.Calculations(list_of_lines)
        analyt = Analytics(list_of_lines)
        predictions_list = analyt.predict_random(config.num_of_steps)
        calc_count_list = calc.counts()
        fractions_list = calc.fractions(calc_count_list)
        heads_predict = sum(1 for head in predictions_list if head[0] == '1')
        tails_predict = sum(1 for tail in predictions_list if tail[0] == '0')
        if heads_predict > 1:
            heads_predict = str(heads_predict) + " heads"
        else:
            heads_predict = str(heads_predict) + " head"

        if tails_predict > 1:
            tails_predict = str(tails_predict) + " tails"
        else:
            tails_predict = str(tails_predict) + " tails"

        report =config.template.format(
            total_observations=len(list_of_lines),
            tails_count=calc_count_list[1],
            heads_count=calc_count_list[0],
            tails_probability=fractions_list[1]*100,
            heads_probability=fractions_list[0]*100,
            forecast_steps=config.num_of_steps,
            tails_predict_full=tails_predict,
            heads_predict_full=heads_predict
            )

        analyt.save_file(report, "report", "txt")
        research.send_message_telegram("The report has been successfully created")
    else:
        research.send_message_telegram("The report hasn't been created due to an error.")
        raise ValueError("Wrong number of arguments!")

