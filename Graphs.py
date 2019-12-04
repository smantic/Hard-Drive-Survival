import matplotlib.pyplot as plt
from lifelines import KaplanMeierFitter
from lifelines import NelsonAalenFitter



durations = [11, 74, 71, 76, 28, 92, 89, 48, 90, 39, 63, 36, 54, 64, 34, 73, 94, 37, 56, 76]
event_observed = [1, 1, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1]

kmf = KaplanMeierFitter()
kmf.fit(durations, event_observed)
kmf.plot(ci_show=False)

plt.title("Hard Drive Kaplan Meier Survival Analysis")
plt.ylabel("Probability a Hard Drive Survives")
plt.show()

naf = NelsonAalenFitter()
naf.fit(durations, event_observed)
naf.plot(ci_show=False)

plt.title("Hard Drive Nelson-Aalen Hazard Estimate")
plt.ylabel("Cumulative Hazard")
plt.show()
