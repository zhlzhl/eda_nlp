# augment cola dataset

from eda import *

# arguments to be parsed from command line
import argparse

ap = argparse.ArgumentParser()
ap.add_argument("--input", required=False, type=str, help="input file of unaugmented data")
ap.add_argument("--output", required=False, type=str, help="output file of unaugmented data")
ap.add_argument("--num_aug", required=False, default=5, type=int,
                help="number of augmented sentences per original sentence")
ap.add_argument("--alpha", required=False, default=0.1, type=float,
                help="percent of words in each sentence to be changed")
args = ap.parse_args()

# augment original file using synonym replacement
def sr_augment(intput_file, output_file, alpha, num_aug=9):
    writer = open(output_file, 'w')
    lines = open(intput_file, 'r').readlines()

    for i, line in enumerate(lines):
        parts = line[:-1].split('\t')
        label = parts[1]        # the second column is label
        sentence = parts[3]     # the fourth column is sentence
        aug_sentences = eda_sr(sentence, alpha_sr=alpha, num_aug=num_aug)
        for aug_sentence in aug_sentences:
            writer.write(parts[0] + "\t" + label + "\t" + parts[2] + "\t" + aug_sentence + '\n')

    writer.close()
    print("generated augmented sentences with synonym replacement for " +
          intput_file + " to " + output_file + " with num_aug=" + str(num_aug))


# main function
if __name__ == "__main__":
    # for testing purpose
    input_file = '/home/user/git/nlp_data/glue/data/CoLA/train.tsv'
    output_file = '/home/user/git/nlp_data/glue/data/CoLA/train_sr.tsv'

    # augment input file using synonym replacement
    sr_augment(input_file, output_file, alpha=0.2, num_aug=3)
