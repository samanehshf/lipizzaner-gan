generations = 10000
n_samples = 5000
output_path = './output-potimization/'

algorithm_ga = 'optimize-ga'
pop_size = 100
mutation_prob = 0.1
crossover_prob = 0.5

algorithm_greddy = 'optimize-greedy'
mode1 = 'random'
mode2 = 'iterative'

algorithm_random = 'optimize-random-search'
# j=0
# for size in range(5,6):
#     for i in range (5,11):
#         for pm in [0.1, 0.2, 0.4]:
#             for pcr in [0.25, 0.50, 0.75]:
#                 j+=1
#                 mutation_prob = pm
#                 crossover_prob = pcr
#                 text = 'time CUDA_VISIBLE_DEVICES={}  python main.py {} -f configuration/quickstart/mnist.yml -o {}/output-{}-{}-{:03d}-{}-{}.txt -e {} --generations {} --n_samples {} --population_size {} -mp {} -cp {} > screen-{}-{}-{:03d}-{}-{}.txt'.format(
#                     j%2, algorithm_ga, output_path, algorithm_ga, size, i, mutation_prob, crossover_prob, size, generations, n_samples,
#                     pop_size, mutation_prob, crossover_prob,
#                     algorithm_ga, size,
#                     i, mutation_prob, crossover_prob)
#
#                 if j%10==0:
#                     print(text)
#                     print('sleep 60')
#                 else:
#                     print(text + '  &')
#



j=0
for size in range(5,10):
    for i in range (0,6):
        text = 'time CUDA_VISIBLE_DEVICES=0  python main.py {} -f configuration/quickstart/mnist.yml -o {}/output-{}-{}-{:03d}.txt -e {} --generations {} --n_samples {} > {}/screen-{}-{}-{:03d}.txt'.format(
            algorithm_random, output_path, algorithm_random, size, i, size, generations,  n_samples, output_path, algorithm_random, size, i)
        j+=1
        if j % 10 == 0:
            print(text)
            print('sleep 60')
        else:
            print(text + '  &')

        # text = 'time CUDA_VISIBLE_DEVICES=0  python main.py {} -f configuration/quickstart/mnist.yml -o {}/output-{}-{}-{}-{:03d}.txt -e {} --n_samples {} --mode {} > screen-{}-{}-{:03d}.txt'.format(
        #     algorithm_greddy, output_path, algorithm_greddy, mode1, size, i, size, n_samples, mode1, algorithm_greddy, size,
        #     i)
        # print(text + ' ')
        # text = 'time CUDA_VISIBLE_DEVICES=0  python main.py {} -f configuration/quickstart/mnist.yml -o {}/output-{}-{}-{}-{:03d}.txt -e {} --n_samples {} --mode {} > screen-{}-{}-{:03d}.txt'.format(
        #     algorithm_greddy, output_path, algorithm_greddy, mode2, size, i, size, n_samples, mode2, algorithm_greddy, size,
        #     i)
        # print(text + ' ')
        #
        # text = 'time CUDA_VISIBLE_DEVICES=0  python main.py {} -f configuration/quickstart/mnist.yml -o {}/output-{}-{}-{:03d}.txt -e {} --generations {} --n_samples {} --population_size {} -mp {} -cp {} > screen-{}-{}-{:03d}.txt'.format(
        #     algorithm_ga, output_path, algorithm_ga, size, i, size, generations, n_samples,
        #     pop_size, mutation_prob, crossover_prob,
        #     algorithm_greddy, size,
        #     i)
        # print(text + ' ')

# for size in range(4, 10):
#     for i in range(0, 5):
#         text = 'time CUDA_VISIBLE_DEVICES=1  python main.py optimize-greedy -f configuration/quickstart/mnist.yml -o output-{}-{}-{:03d}.txt -e {} --mode {} > screen-{}-{}-{:03d}.txt'.format(mode2, size, i, size, mode2, mode2, size, i)
#         print(text)