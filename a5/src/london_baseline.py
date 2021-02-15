# Calculate the accuracy of a baseline that simply predicts "London" for every
#   example in the dev set.
# Hint: Make use of existing code.
# Your solution here should only be a few lines.

import argparse
import utils

if __name__ == "__main__":

    argp = argparse.ArgumentParser()
    argp.add_argument('--eval_corpus_path',
        help="Path of the corpus to evaluate on", default=None)
    args = argp.parse_args()

    correct = 0
    total = 0
    predictions = ["London" for line in open(args.eval_corpus_path)]
        
    total, correct = utils.evaluate_places(args.eval_corpus_path, predictions)
    print(f"Total: {total}")
    print(f"Correct: {correct}")
    print(f"Accuracy: {correct/total}")