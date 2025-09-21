import matplotlib.pyplot as plt

def plot_timeseries(ts, col, title="Timeseries"):
    ts[col].plot(title=title)
    plt.xlabel("Date")
    plt.ylabel(col)
    plt.tight_layout()
    plt.show()
