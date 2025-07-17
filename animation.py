import matplotlib.pyplot as plt
import matplotlib.animation as animation
import pandas as pd


def setup_plot_style(ax):
    ax.set_xlabel('Female Population')
    ax.set_ylabel('Country')
    ax.set_title('Top 10 Countries by Female Population')

def add_year_text(ax, year):
    ax.text(0.9, 0.1, str(year), transform=ax.transAxes, ha='center', fontsize='14')

def create_animation(df):
    df = pd.read_csv("cleaned_data.csv")

    frames = df['Time'].unique()

    fig, ax = plt.subplots(figsize=(10, 6))

    def animate(frame):
        ax.clear()
        data_frame = df[df['Time'] == frame]

        top_countries = data_frame.nlargest(10, 'TPopulationFemale1July').sort_values(by='TPopulationFemale1July', ascending=True)  

        ax.barh(top_countries['Location'], top_countries['TPopulationFemale1July'], edgecolor='black')
        setup_plot_style(ax)
        add_year_text(ax, frame)
        plt.tight_layout()
    
    anim = animation.FuncAnimation(fig, animate, frames=frames, interval=100)
    return anim

if __name__ == "__main__":
    df = pd.read_csv("cleaned_data.csv")
    anim = create_animation(df)
    anim.save('animation.gif', writer='pillow', fps=10)
    plt.show()


