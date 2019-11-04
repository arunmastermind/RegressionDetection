# import csv
# import numpy as np
# with open('regressionData.csv','w') as file:
#     # writer = csv.writer(file, delimiter=',')
#     for a in np.arange(0, 5, 0.001):
#         for b in np.arange(0, 5, 0.001):
#             for c in np.arange(0, 5, 0.001):
#                 for d in np.arange(0, 5, 0.001):
#                     for e in np.arange(0, 5, 0.001):
#                         for f in np.arange(0, 5, 0.001):
#                             for g in np.arange(0, 5, 0.001):
#                                 x = (f'{a:.1f}, {b:.1f}, {c:.1f}, {d:.1f}, {e:.1f}, {f:.1f}, {g:.1f}\n')
#                                 print(f'PRESENT ITERATION :: {x}')
#                                 file.write(x)




import csv
import numpy as np
with open('regressionData.csv','w') as file:
    # writer = csv.writer(file, delimiter=',')
    for a in np.arange(0, 1000001, 1):
        for b in np.arange(0, 1000001, 1):
            for c in np.arange(0, 1000001, 1):
                for d in np.arange(0, 1000001, 1):
                    for e in np.arange(0, 1000001, 1):
                        for f in np.arange(0, 1000001, 1):
                            for g in np.arange(0, 1000001, 1):
                                x = (f'{a:.3f}, {b:.3f}, {c:.3f}, {d:.3f}, {e:.3f}, {f:.3f}, {g:.3f}, {0.000}\n')
                                # x = "a"
                                print(f'PRESENT ITERATION :: {x}')
                                file.write(x)