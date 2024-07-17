


import numpy as np
import matplotlib.pyplot as plt

import random
import sys

def trial(prob, num):
    final_sum = 0
    history = [final_sum]
    num_of_ones = 0
    for i in range(num):
        if random.random() < prob:
            final_sum += 1
            num_of_ones += 1
        else:
            final_sum -= 1
        history.append(final_sum)

    # sys.stdout.write('num of  1: ' + str(num_of_ones) + '\n')
    # sys.stdout.write('num of -1: ' + str(num - num_of_ones) + '\n\n')

    return (final_sum, history)
    

def main(prob, num, num_of_trials):

    samples_of_sum = []
    history = []

    for j in range(num_of_trials):
        (sum_of_results, results) = trial(prob, num)
        samples_of_sum.append(sum_of_results)
        history.append(results)

    (counts, bins) = np.histogram(samples_of_sum, bins=20)
    

    fig = plt.figure()
    ax1 = fig.add_subplot(211)
    for j in range(num_of_trials):
        ax1.plot(np.arange(0, num + 1), history[j], '-', label=str(j))
    ax1.legend()

    ax2 = fig.add_subplot(212)
    ax2.stairs(counts, bins)
    
    plt.show()
    fig.close()    
        

if __name__ == '__main__':

    prob = 0.5
    num = 100
    num_of_trials = 100
    
    if len(sys.argv) != 4:
        sys.stderr.write('Usage: python3 ' + sys.argv[0] + ' <probability of 1> <num of samples> <num of trials>\n')
        sys.exit()
        
    prob = float(sys.argv[1])
    num = int(sys.argv[2])
    num_of_trials = int(sys.argv[3])
    
    main(prob, num, num_of_trials)

