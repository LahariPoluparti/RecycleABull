# RecycleABull

This is a web application that specifies if a certain type of plastic is recyclable or not by reflecting different wavelengths of light. This project was made at Swamphacks with a total of four students.

**Inspiration:**
Americans represent 5% of the world’s population but generate 30% of the world’s garbage. Moreover, about 80% of what Americans throw away is recyclable, yet our recycling rate is only 28%. Especially, plastics that could be recyclable take thousands of years to decompose which might affect the sea animals like turtles as they try to eat them. Considering all the potential hazards and leaning more towards a more eco-friendly life has inspired us to make a web application that would eliminate the misuse of plastics.

**How we build it:**
We made the web application using flask for our backend and HTML, CSS, Bootstrap, and Javascript for the frontend. We also built a hardware device using an ESP32 Feather and a AS7265X spectral sensor. This gave us the wavelength needed to identify different plastics. Then, we created our own dataset by scanning different plastics and sent raw values from the sensor to be processed and stored. We stored the values on Firebase and processed them using Python and SciKit Learn. This gave us the classification that we needed to know if you could recycle the object or not. 

**Challenges we ran into:**
The first challenge we faced was collecting the datasets. Because we decided to create our own data set, we had to obtain 70 different datasets. The second challenge we faced was recalibrating the sensor. Due to time constraints, it was difficult to obtain all the databases we have collected. The third challenge we faced was working with technologies like flask, bootstrap, and firebase because it was not familiar with most of the members in the group. Therefore, we had to learn it before executing the project.


In order to know more about the project and access the hardware we made, please visit my devpost. The URl is right here:
[GitHub Pages](https://devpost.com/software/recycler-62ndj3)
