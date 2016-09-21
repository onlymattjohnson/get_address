## get_address

get_address is a command line python script that allows a user to get a properly formatted address from the command line

## Code Example

    $ ./get_address.py White House, Washington DC
    $ The White House, 1600 Pennsylvania Ave NW, Washington, DC 20500, US

    $ ./get_address.py 11 Wall Street. New York
    $ 11 Wall St, New York, NY 10005, USA

## Motivation

I created this script because I found myself needing to look up zip codes for manual data entry 
processes at work. I got tired of opening google maps and searching it, so I just dump it into the 
command line now.

## Installation

You can run this as a script on it's own or copy it to your bin directory. You will need to install 
the geocoder library:

    $ pip install geocoder

## Contributors

Feel free to fork this project and make use of it as you will.

## License

This software is licensed under the GNU General Public LIcense v3.0; See included LICENSE.md for 
details
