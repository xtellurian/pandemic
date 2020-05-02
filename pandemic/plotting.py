from pandemic.conventions import STATE_DESCRIPTIONS
from collections import Counter
import matplotlib.pyplot
from pandemic.example_parameters import TOY_TOWN
from pandemic.configuration import load_configuration

config = load_configuration()

def render(plt: matplotlib.pyplot, day= None):
    if not config.headless:
        plt.show(block=False)
        plt.pause(0.01)

    if config.save_plt:
        if day is None:
            plt.savefig(f'{config.plt_output}/img_{render.counter}.png')
            render.counter = render.counter + 1
        else:
            plt.savefig(f'{config.plt_output}/img_day_{day}.png')
render.counter = 0


def plot_callback( positions, status, params, day, day_fraction, home, work, plt, xlabel, step_no, plot_hourly ):
    if plt and (plot_hourly or step_no % 12 == 0):
        plt.clf()
        plot_points(plt=plt, positions=positions, status=status,
                    title="Day " + str(day) + ':' + str(int(100*day_fraction)/100).zfill(4))
        b = params['geometry']['b']
        plt.axis([-b, b, -b, b])
        if xlabel:
            plt.xlabel(xlabel)

        render(plt, day)


def plot_points(plt, positions, status, title=None, sizes=None):
    x = [p[0] for p in positions]
    y = [p[1] for p in positions]
    if status is not None:
        if sizes is None:
            if len(positions)>TOY_TOWN['geometry']['n']:
                sizes = [ 1,  16,  9,  9, 4,  16 ]
            else:
                sizes = [ 100, 100, 100, 100, 100, 100]
        scatter = plt.scatter(x=x, y=y, c=status, alpha=0.7, s=[ sizes[s]+4 for s in status ] )
        running = Counter(status)
        descriptions = list(STATE_DESCRIPTIONS.values())
        running_totals  = [ (descriptions[k]+ " ("+str(v)+")",k) for k,v in running.items() ]
        running_totals.sort( key=lambda rt: rt[1] )
        labels = [ desc for desc,_ in running_totals ]
        plt.legend(handles=scatter.legend_elements()[0], labels=labels, loc='upper left')
        if title:
            plt.title(title)
    else:
        scatter = plt.scatter(x=x, y=y)
    return scatter
