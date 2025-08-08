# Ternary plots

This script uses matplotlib to plot ternary trajectories that usually appear in the field of evolutionary game theory.

---

### **Overview**

This script is a tool I developed to plot graphs for my master's degree. I wrote the code to be easily importable and reusable, allowing me to use it in other projects without making changes to the original file. I've polished it a bit and am now sharing it in case it's useful to others.

_Note_: I am not a professional Python developer. I cannot guarantee that the script will work in all situations, so please use it at your own risk.

---

## **How to use it**

You're welcome to use the script as it is, but if you just need some simple plots and want to avoid diving into the code, you can simply import it and use the methods I'll describe below

#### **Prerequisites**

* matplotlib

### Example ###
Let's suppose we have three files, each one of them containing a trajectory. The plot could be written like this:
<pre>
import ternaryplot as tp

tp.set_axis(("A", "B", "C"))
tp.set_title("Three Strategies")

tp.plot("data1.txt", 
        show_arrow = True, 
        arrow_pos = 45, 
        line_color = "#CC3311", 
        label = "Trajectory 1")

tp.plot("data2.txt", 
        show_arrow = True, 
        arrow_pos = 20, 
        line_color = "#009988", 
        label = "Trajectory 2")

tp.plot("data3.txt", 
        show_arrow = True, 
        arrow_pos = 25, 
        line_color = "#0077BB", 
        label = "Trajectory 3")

tp.show_legend(font_size = 12)
tp.save("image.png")
tp.show()

</pre>

which produces the output

<figure style = "text-align : center;">
<img src="trajectories.png" alt="Three strategies" width="400"/>
<figcaption>Three different trajectories of a Rock-Paper-Scissors Game.</figcaption>
</figure>

## The "Documentation" ##
