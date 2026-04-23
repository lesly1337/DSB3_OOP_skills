import sys
from analytics import Research, Analytics
import config
if __name__ == '__main__':
    if (len(sys.argv) == 2):
        research = Research(sys.argv[1])
        list_of_lines = research.file_reader()
        calc = research.Calculations(list_of_lines)
        analyt = Analytics(list_of_lines)
        predictions_list = analyt.predict_random(config.num_of_steps)
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
            tails_count=calc.counts()[1],
            heads_count=calc.counts()[0],
            tails_probability=calc.fractions(calc.counts())[1]*100,
            heads_probability=calc.fractions(calc.counts())[0]*100,
            forecast_steps=config.num_of_steps,
            tails_predict_full=tails_predict,
            heads_predict_full=heads_predict
            )

        analyt.save_file(report, "report", "txt")
    else:
            raise ValueError("Wrong number of arguments!")

