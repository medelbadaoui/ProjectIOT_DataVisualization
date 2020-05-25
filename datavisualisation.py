from storedata import sensor_Data_Getter
from storedata import get_Temperature_Level
from storedata import get_Humidity_Level
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
from datetime import datetime






format = '%d-%b-%Y %H:%M:%S:%f'
fig = plt.figure()
fig.set_size_inches(18.5, 10.5, forward=True)
    


#---------------------------------------------------------------------
def animate(i):
    # Create figure for plotting
    data_temperature=sensor_Data_Getter("Home/Bedroom/DHT1/Temperature")

    xs = []
    ys = []

    for recordtemp in data_temperature:
        xs.append(datetime.strptime(recordtemp[2], format).strftime('%d-%b %H:%M:%S'))
        ys.append(recordtemp[3])

    
    
    ax =fig.add_subplot(3, 4, 1)
    ax.clear()
    ax.plot(xs, ys)

    plt.xticks(rotation=90, ha='right')
    plt.subplots_adjust(bottom=0.30)
    plt.title('Temperature Over Time')

    plt.ylabel('Temperature')
    #------------------
    data_humidity=sensor_Data_Getter("Home/Bedroom/DHT1/Humidity")
    xs1=[]
    ys1=[]

    for recordhumi in data_humidity:
        xs1.append(datetime.strptime(recordhumi[2], format).strftime('%d-%b %H:%M:%S'))
        ys1.append(recordhumi[3])


    ax1=fig.add_subplot(3, 4, 9)
    ax1.clear()
    ax1.plot(xs1,ys1)


    plt.xticks(rotation=90, ha='right')
    plt.subplots_adjust(bottom=0.30)
    plt.ylabel('Humidity ')
    plt.title('Humidity Over Time')
    # Draw the graph
    #------------------
    data_acc=sensor_Data_Getter("Home/Bedroom/DHT1/Acceleration")
    xs2=[]
    ys2=[]
    xs3=[]
    ys3=[]
    for recordacc in data_acc:
        xs2.append(datetime.strptime(recordacc[2], format).strftime('%d-%b %H:%M:%S'))
        ys2.append(recordacc[3])
        xs3.append(datetime.strptime(recordacc[2], format).strftime('%d-%b %H:%M:%S'))
        ys3.append(recordacc[4])


    ax2=fig.add_subplot(3, 4, 12)
    ax2.clear()
    ax2.plot(xs2,ys2)


    plt.xticks(rotation=90, ha='right')
    plt.subplots_adjust(bottom=0.30)
    plt.ylabel('Accelerator X ')
    plt.title('Acceleration X Over Time')


    # Draw the graph
    #----------------------
    


    ax3=fig.add_subplot(3, 4, 4)
    ax3.clear()
    ax3.plot(xs3,ys3)


    plt.xticks(rotation=90, ha='right')
    plt.subplots_adjust(bottom=0.30)
    plt.ylabel('Accelerator Y ')
    plt.title('Acceleration Y Over Time')
    # Draw the graph

    #------------------------------ pie charts
    ax4=fig.add_subplot(3, 4, 10)
    labels = 'VERY COLD', 'COLD', 'NORMAL', 'HOT','VERY HOT'
    sizes = [get_Temperature_Level('VERY COLD'),get_Temperature_Level('COLD'),get_Temperature_Level('NORMAL'),get_Temperature_Level('HOT'),get_Temperature_Level('VERY HOT')]
    explode = (0, 0, 0, 0,0)  # only "explode" the 2nd slice (i.e. 'Hogs')
    ax4.clear()
    ax4.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
    ax4.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    plt.title('Temperature Data per Level')
    #----------------------------------------------------------
    ax5=fig.add_subplot(3, 4, 2)
    labels1 = 'LOW', 'MEDIUM', 'HIGH'
    sizes1 = [get_Humidity_Level('LOW'), get_Humidity_Level('MEDIUM'),get_Humidity_Level('HIGH') ]
    explode1 = (0, 0, 0)  
    ax5.clear()
    ax5.pie(sizes1, explode=explode1, labels=labels1, autopct='%1.1f%%',
        shadow=True, startangle=90)
    ax5.axis('equal')
    plt.title('Humidity Data per Level')  # Equal aspect ratio ensures that pie is drawn as a circle.


ani= animation.FuncAnimation(fig, animate, interval=1000)
plt.show()
# Draw the graph



    
 
        