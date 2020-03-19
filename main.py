from text import text
from punctuation import punctuation
import matplotlib.pyplot as plt


class FrequencyAnalysisClass:
    def __init__(self):
        self.algorithm()

    def clean_my_text(self):
        self.clean_text = []
        text_as_a_list = list(text.lower())
        for index in range(0, len(text_as_a_list)):
            if text_as_a_list[index] not in punctuation:
                self.clean_text.append(text_as_a_list[index])
        alphabets_set_found = set(self.clean_text)
        self.final_list_of_alphabets_found = list(alphabets_set_found)
        self.final_list_of_alphabets_found.sort()

    def count_number_of_alphabets(self):
        self.count_of_alphabets_found = list(
            map(lambda to_find: self.clean_text.count(to_find), self.final_list_of_alphabets_found))

    def find_frequency_of_alphabets(self):
        self.frequency_of_alphabets_found = list(map(lambda x: x / len(self.clean_text), self.count_of_alphabets_found))

    def plot_two_graphs_in_one(self):
        zipped_list = list(zip(self.final_list_of_alphabets_found,
                               self.frequency_of_alphabets_found))
        res = sorted(zipped_list, key=lambda x: x[1], reverse=True)
        alpha, freq = [], []
        for item in res:
            alpha.append(item[0])
            freq.append(item[1])
        plt.subplot(2,1,1)
        plt.bar(alpha,
                freq,
                label='Frequencies',
                color='b')
        plt.xlabel('Alphabets')
        plt.ylabel('Frequency')
        plt.title('Frequencies in Descending order')
        plt.legend()

        plt.subplot(2,1,2)
        plt.bar(self.final_list_of_alphabets_found,
                self.frequency_of_alphabets_found,
                label='Frequencies',
                color='red')
        plt.xlabel('Alphabets')
        plt.ylabel('Frequency')
        plt.title('Frequency analysis')
        plt.legend()
        plt.tight_layout(pad=2)
        plt.show()

    def algorithm(self):
        self.clean_my_text()
        self.count_number_of_alphabets()
        self.find_frequency_of_alphabets()
        self.plot_two_graphs_in_one()


if __name__ == "__main__":
    obj = FrequencyAnalysisClass()
