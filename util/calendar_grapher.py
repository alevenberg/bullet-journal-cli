import calendar
import numpy as np
from matplotlib.patches import Rectangle
import matplotlib.pyplot as plt


# def plot_calendar(year, dates):
#     plt.title('Calendar' + year)
#     plt.savefig('./graph/calendar.png')

# def plot_calendar_year(dates):
#     """ 
#     Plots the specific dates

#     Args: 
#         dates (list of date time objects) 

#     Returns:
#         the generated plot without a title
#     """
#     plot_calendar_year = plot_calendar_year# split 

def plot_calendar_year(days, months):
    """
    Plots the whole year with specified days as blue
    The invalid days are gray and everything else is white 
   
    Args:
        days (list): a list of days, expects 1-31
        months (list): the corresponding list of months, expects 1-12 

    Returns:
        the generated plot without a title
    """
    plt.figure(figsize=(9, 3))

    # Invalid days are grayed
    ax = plt.gca().axes
    ax.add_patch(Rectangle((29, 2), width=.8, height=.8, 
                           color='gray', alpha=.3))
    ax.add_patch(Rectangle((30, 2), width=.8, height=.8,
                           color='gray', alpha=.5))
    ax.add_patch(Rectangle((31, 2), width=.8, height=.8,
                           color='gray', alpha=.5))
    ax.add_patch(Rectangle((31, 4), width=.8, height=.8,
                           color='gray', alpha=.5))
    ax.add_patch(Rectangle((31, 6), width=.8, height=.8,
                           color='gray', alpha=.5))
    ax.add_patch(Rectangle((31, 9), width=.8, height=.8,
                           color='gray', alpha=.5))
    ax.add_patch(Rectangle((31, 11), width=.8, height=.8,
                           color='gray', alpha=.5))
    for d, m in zip(days, months):
        ax.add_patch(Rectangle((d, m), 
                               width=.8, height=.8, color='C0'))
    plt.yticks(np.arange(1, 13)+.5, list(calendar.month_abbr)[1:])
    plt.xticks(np.arange(1,32)+.5, np.arange(1,32))
    plt.xlim(1, 32)
    plt.ylim(1, 13)
    plt.gca().invert_yaxis()
    
    # Remove borders and ticks
    for spine in plt.gca().spines.values():
        spine.set_visible(False)
    plt.tick_params(top=False, bottom=False, left=False, right=False)
    return plt

# Source 
# https://dzone.com/articles/plotting-a-calendar-in-matplotlib