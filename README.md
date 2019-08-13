# onkyo-rpi
Command line tool to control ONKYO devices connected to Raspberry Pi via Remote Interactive protocol. This project was mainly inspired by a similiar project for the arduino plattform [Onkyo-RI](https://github.com/docbender/Onkyo-RI). Thanks to [docbender](https://github.com/docbender) for digging out the [protocol description](http://fredboboss.free.fr/articles/onkyo_ri.php) from the web. :)

# Send message
The script ```main.py``` accepts a message as parameter from 0-4095 as hex or int (12 bits) which you want to send to your device.

Example:
```bash
# sends turn off message to device
python main.py 0x1AE
# you can additionally pass a gpio port as parameter
python main.py --gpio 25 0x1AE
```

# Scan for supported messages
With the script ```scan.py``` can you find out which messages your device reacts to. You can parameterize the lower and upper boundaries of your scan, the gpio port to use and the delay between sent messages. Run the script and check your device for changes.

Example:
```bash
# scan from 0x000 to 0xFFF
python scan.py --gpio 25
# set boundaries
python scan.py --lower 0x120 --upper 0x12F
# increase delay in seconds between sent messages
python scan.py --delay 1
```

# Known messages
I am using an **Onkyo TX-SR500E AV Receiver** and following messages lead to actions on the device.
<table>
    <tbody>
        <tr>
            <td> <b>Message</b> </td>
            <td> <b>Action</b> </td>
        </tr>
        <tr>
            <td> 0x070 </td>
            <td> switch to mode TAPE </td>
        </tr>
        <tr>
            <td> 0x07F </td>
            <td> turn on and switch to mode TAPE </td>
        </tr>
        <tr>
            <td> 0x120 </td>
            <td> switch to mode DVD </td>
        </tr>
        <tr>
            <td> 0x12F </td>
            <td> turn on and switch to mode DVD </td>
        </tr>
        <tr>
            <td> 0x1A0 </td>
            <td> switch to mode VIDEO2 </td>
        </tr>
        <tr>
            <td> 0x1A2 </td>
            <td> volume up </td>
        </tr>
        <tr>
            <td> 0x1A3 </td>
            <td> volume down </td>
        </tr>
        <tr>
            <td> 0x1A4 </td>
            <td> mute </td>
        </tr>
        <tr>
            <td> 0x1A5 </td>
            <td> unmute </td>
        </tr>
        <tr>
            <td> 0x1AE </td>
            <td> turn off device </td>
        </tr>
        <tr>
            <td> 0x1AF </td>
            <td> turn on and switch to mode VIDEO2 </td>
        </tr>
    </tbody>
</table>

# Connection
The connection to the RI interface is a simple 3.5 mm mono headphone jack. Connect the tip of the jack to a GPIO output pin (default: 25) and the ground of the jack to a ground pin on your raspberry pi.