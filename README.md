# Doorbell Dash
- An Internet of Things device implementing Raspberry Pi, Amazon Dash Buttons, Python 3, IFTTT and Imgur API. 
- A Wi-Fi enabled doorbell using an Amazon Dash button, that when pressed, takes a photo with the Raspberry Pi camera and sends an IFTTT notification to your phone with an Imgur link. 

## What you'll need
* Amazon Dash Button ($1 - $5)
* Raspberry Pi
* Pi-camera
* IFTTT account for notifications (free)
* Imgur account for images (free)

## Installation on your Raspberry Pi
* $ <code>pip3 install scapy-python3</code>
* $ <code>pip install pyimgur</code>
* $ <code>pip install requests</code>

## 'Hack' Amazon Dash Button
* Open the Amazon Shopping app on your PHONE.
* From the menu, GOTO 'Your Account'
* Scroll down, choose 'Set up a new device'
* Choose 'Dash Button'
* Connect your button to your local wifi network
* Do NOT choose a product to order, just exit the app.

## Discover the Dash Button's MAC address
- Push button for 3 seconds until it pulses blue
- Connect your computer wifi to "Amazon ConfigureMe"
- In a web browser, go to: http://192.168.0.1/
- Make note of the MAC address of your Dash Button. Note: For the python code, MAC address needs to be all lower case!

## Setup IFTTT Account
To receive IFTTT notifications you'll need to create an account on IFTT.com account

1. Visit https://ifttt.com/create
1. Click on "This"
1. Select "Webhooks"
1. Select "Receive web request"
1. Enter the event name
1. Click "Create"
1. Click on "That"
1. Select "Notifications"
1. Select "Send a notification from the IFTTT app"
1. Paste in the following: "Doorbell has been pressed {{Value1}}"
1. Click "Create Action"
1. Click "Finish"
1. Visit https://ifttt.com/maker_webhooks
1. Copy + paste the event url into the .env file (https://maker.ifttt.com/trigger/{event_name_you_set}/with/key/YOURUNIQUEKEY)
1. Install the IFTTT app on your phone and sign in.

## General Notes
* !! <strong> RENAME ExampleCreds.py to creds.py </strong> !! Put in all the information you received from Imgur and Twilio here. This will store all personal information (phone numbers, API tokens, etc).  This is not in the project, as it is in the gitignore.
* ARP (Address Resolution Protocol) is used for mapping a network address to a physical address. EXAMPLE:  IP Address to a MAC address.
* Problems with Raspberry Pi and camera communicating? Check to make sure your Pi detects the camera: <br>
  <code>$vcgencmd get_camera</code>

## Update Raspberry Pi
* It's a good idea to update your Pi to make sure the packages you install are up to date.
* <code>$ sudo apt-get update</code>
* <code>$ sudo apt-get dist-upgrade</code>

## If you run into errors updating your Pi, you may need to change your python version system-wide.  
* $ <code>python --version</code>
* $ <code>update-alternatives --list python</code>
* $ <code>sudo update-alternatives --config python</code>

## Usage
* You must run script as root user / SUDO
* $ <code>SUDO python arp.py</code>
* For the doorbell to work, keep this script running.  
* arp.py runs a packet sniffer on your local network looking for MAC addresses that are linked to Amazon Dash Buttons.

## Contributing
1. Fork it!
2. Create your feature branch: `git checkout -b my-new-feature`
3. Commit your changes: `git commit -am 'Add some feature'`
4. Push to the branch: `git push origin my-new-feature`
5. Submit a pull request

## Credits
* Nick Chemsak
* Brian Dauernheim

## License
[MIT License](https://github.com/nchemsak/doorbell_dash_angularJS/blob/master/LICENSE)


