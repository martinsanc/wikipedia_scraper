import geopandas
import matplotlib.pyplot as plt
import seaborn as sns
import os


def plot_world(df, col, title):
    world = geopandas.read_file(geopandas.datasets.get_path('naturalearth_lowres'))
    col_name = df.columns[col]
    world = world.merge(df, left_on='name', right_on='Country')
    world[col_name] = world[col_name].astype(float)
    world.plot(column=col_name, legend=True)
    plt.title(title)

    path = "../viz/" + title + ".png"
    if not os.path.exists(os.path.dirname(path)):
        # Crea directorio si no existe
        os.makedirs(os.path.dirname(path))

    plt.savefig(path)
    plt.show()


def plot_2cols(df, x, y, title, x_label=None, y_label=None):
    x_name = df.columns[x]
    y_name = df.columns[y]
    df[x_name] = df[x_name].astype(float)
    df[y_name] = df[y_name].astype(float)
    sns.scatterplot(data=df, x=x_name, y=y_name)
    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)

    path = "../viz/" + title + ".png"
    if not os.path.exists(os.path.dirname(path)):
        # Crea directorio si no existe
        os.makedirs(os.path.dirname(path))

    plt.savefig(path)
    plt.show()
