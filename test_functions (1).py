"""Test for my functions.

Note: because these are 'empty' functions (return None), here we just test
  that the functions execute, and return None, as expected.
"""

from functions import *

#source: https://stackoverflow.com/questions/35851323/how-to-test-a-function-with-input-call
def test_prediction_question(monkeypatch):
    assert callable(prediction_question)
    monkeypatch.setattr('builtins.input', lambda _: "Good")
    prediction = input("How well do you think you'll do, peasant? ")
    assert prediction == "Good"

def test_checking_answer(answer = 'c', text = 's'):
    assert callable(checking_answer)
    assert checking_answer(answer = answer, text = text) == 0
    assert checking_answer(answer = answer, text = 'c') == 1

def test_final_score(score = 5, inputs = 'cbabd', prediction = "Good"):
    assert callable(final_score)
    assert final_score(score = score, inputs = inputs, prediction = prediction) == print("~~~~~~~~~~~~~~~~\nJudgement day (ง’̀-‘́)ง:\n" + 
      "~~~~~~~~~~~~~~~~\nAnswers:  c b a b d \n" +
      "Inputs: c b a b d \n" +
      "Your Prediction: Good\n" +
      "Conclusion: You cheated (ಠ_ಠ).\n" +
      "Total Score: 5")