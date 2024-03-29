# Raspberry Pi kill switch

This is a project to create a [physical](https://en.wikipedia.org/wiki/Scram) [kill switch](https://en.wikipedia.org/wiki/Kill_switch) for the [Raspberry Pi](https://www.raspberrypi.org/) (Specifically the [Model 3](https://www.raspberrypi.org/products/raspberry-pi-3-model-b/)). It's got a 3-colour LED included to give some status information as it does its job.

## Background

I used a Raspberry Pi along with [shairport-sync](https://github.com/mikebrady/shairport-sync) to play music wirelessly in my living room. However, sometimes I want to turn off the music in a hurry, and I don't know which device (phone, laptop, my wife's phone, etc) is streaming sound to the speaker. This led to the idea of a physical switch connected to the Raspberry Pi which would kill the music immediately.

## The finished product
<img src="images/IMG_2508.jpeg" width="425" title="Button"> <img src="images/IMG_2518.jpeg" width="425" title="Full thing">

## Materials required
* [Raspberry Pi Model 3](https://www.raspberrypi.org/products/raspberry-pi-3-model-b/)
* A [button](https://www.amazon.de/dp/B0814N7CH3/ref=sr_1_11?keywords=arduino+taster&qid=1585509555&sr=8-11)
* A cap from a moisturiser jar
* A [3-colour LED module](https://www.amazon.de/dp/B07V6YSGC9/ref=sr_1_3?keywords=arduino+rgb+led+modul&qid=1585509606&sr=8-3)
* Some ribbon cable
* A 10kΩ resistor
* Soldering iron
* Small circuit board and connectors

## Design
This took two attempts to get right. (Go look through the `git` history if you dare).

The Raspberry Pi runs a [Python script](./scripts/killswitch.py) which listens for `GPIO` input events on Pin 10. Whenever the pin switches from `GPIO.LOW` to `GPIO.HIGH` - we act on this and run the task that kills the required process.

Originally I didn't understand the problem of a "floating" pin, which meant that the GPIO pin was not connected to any circuit, unless the switch was pressed. This made it act like an antenna, and randomly reported it's state as GPIO.HIGH due to electrical interference. This often happened due to nearby high-current motors like a sewing machine, or vacuum cleaner.

Second time around, I designed the circuit correctly, based on the two referenced links at the end. The GPIO Pin 10 is connected to `GND` usually, through a 10kΩ resistor. When the button is pressed, this circuit is instead made directly to the 3.3V output, which signals `HIGH`.

## Assembly Instructions
I started by drilling through the moisturiser jar cap, to have somewhere to mount the button. I previously used one of these for my [water level indicator](https://github.com/skhg/water-filter-sensor) so it was another chance to have a nice plain mount for something. Underneath, i mounted the LED module and soldered the wires to the button terminals. In all, 6 wires are required for the button and the LED module.

<img src="images/IMG_2505.jpeg" width="425" title="Button underside"> <img src="images/IMG_2623.jpeg" width="425" title="Open Raspi">

The LED module has some built-in resistors so it can be hooked up to a normal 3.3V GPIO pin without any other components required. But the button needs a resistor to ensure we don't blow the circuit if it was pressed too long or shorted. So the next step was to assemble a mini board that will mount on to the Raspberry Pi's GPIO pins.

<img src="images/killswitch_bb.png" title="Circuit diagram">

And the finished adapter board:

<img src="images/IMG_2511.jpeg" width="425" title="Board view 1"> <img src="images/IMG_2512.jpeg" width="425" title="Board view 2">

Once this was put together, it was as easy as connecting the ribbon cable up, and plugging in the power. Here it's installed and everything else tidied away:

<img src="images/IMG_2519.jpeg" title="Installed">

## Running the software
Requirements: An executable script to do the "killing" must be present at `~/.killswitch`

The software is made of two Python scripts. One is a [event listener](scripts/killswitch.py) that runs forever, and waits for an interrupt on the GPIO input pin. The other is a [utility](scripts/lightControl.py) that can be run from anywhere, to set the currently displayed light colour.

The listener is triggered by the GPIO interrupt on pin 10. When that happens, the killswitch script executes the contents of `~/.killswitch`. In my case I want to kill my streaming music server so the content of `~/.killswitch` is:

```sh
#!/usr/bin/env bash

sudo systemctl restart shairport-sync
```

I also want to know when music is playing and make use of the 3-colour LED module. So the `shairport-sync` config file comes in handy here. It is set up to call my `lightControl.py` script whenever music starts or stops.

Note: To control GPIO from `shairport-sync`, its user must be in the `gpio` group. This was also a factor in [another project](https://github.com/skhg/shairport-power). Run this command to fix it if you have problems:

```
sudo adduser shairport-sync gpio

```

## References

Some useful references which could help when doing this project

* https://raspberrypihq.com/use-a-push-button-with-raspberry-pi-gpio/
* https://www.electronicwings.com/raspberry-pi/raspberry-pi-gpio-access
* https://www.instructables.com/id/Using-a-RPi-to-Control-an-RGB-LED/
* https://grantwinney.com/using-pullup-and-pulldown-resistors-on-the-raspberry-pi/
* https://www.kalitut.com/2017/11/RaspberryPi-GPIO-pull-up-pull-down-resistor.html
