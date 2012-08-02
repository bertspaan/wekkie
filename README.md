
- sudo locale-gen en_US en_US.UTF-8 en_GB en_GB.UTF-8
- dpkg-reconfigure locales
- sudo nano /etc/network/interfaces

		auto wlan0
		iface wlan0 inet dhcp
			wpa-conf /etc/wpa_supplicant.conf	

- sudo nano /etc/wpa_supplicant.conf

		network={
			scan_ssid=1
			ssid="Sitecom54D7FA"
			proto=WPA
			key_mgmt=WPA-PSK
			pairwise=CCMP
			group=CCMP
			psk="55PJUFWYZG84"
		}

- sudo apt-get install git
- sudo apt-get install subversion
- sudo apt-get install redis-server
- sudo apt-get install netatalk
- sudo apt-get install avahi-daemon
- sudo update-rc.d avahi-daemon defaults
- sudo nano /etc/avahi/services/afpd.service

		<?xml version="1.0" standalone='no'?><!--*-nxml-*-->
		<!DOCTYPE service-group SYSTEM "avahi-service.dtd">
		<service-group>
		   <name replace-wildcards="yes">%h</name>
		   <service>
		      <type>_afpovertcp._tcp</type>
		      <port>548</port>
		   </service>
		</service-group> 

- sudo /etc/init.d/avahi-daemon restart
- sudo nano /etc/avahi/services/rfb.service

    	<?xml version="1.0" standalone='no'?>
		<!DOCTYPE service-group SYSTEM "avahi-service.dtd">
		<service-group>
		  <name replace-wildcards="yes">%h</name>
		  <service>
		    <type>_rfb._tcp</type>
		    <port>5901</port>
		  </service>
		</service-group>

- sudo /etc/init.d/avahi.deamon restart
- sudo apt-get install ca-certificates
- sudo wget http://goo.gl/1BOfJ -O /usr/bin/rpi-update && chmod +x /usr/bin/rpi-update
- //rpi-update

- sudo apt-get install python-dev
- sudo apt-get install python-pip
- sudo apt-get install libasound-dev
- sudo apt-get install portaudio19-dev
- sudo apt-get install cython
- libssl-dev zlib1g-dev libvorbis-dev libtool libncursesw5-dev libao-dev
- apt-get install libao-dev
- sudo apt-get install sox

mkdir dev
svn co https://despotify.svn.sourceforge.net/svnroot/despotify despotify



despotify

https://developer.spotify.com/technologies/libspotify/#download
make install

- sudo easy_install pyaudio
- sudo easy_install pyechonest
- sudo easy_install hotqueue
- sudo easy_install pyspotify



sudo pip install -U pyspotify==dev

Start wekkie_alarm and wekkie_player.

Test: ./wekkie_recorder.py -s "14:44 met Josh Ritter"
(For now, use 24 hour time format)

Create configuration file
wekkie.cfg

[spotify]
user = {user}
password = {password}