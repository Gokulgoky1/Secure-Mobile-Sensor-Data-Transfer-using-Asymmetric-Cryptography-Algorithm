# Secure-Mobile-Sensor-Data-Transfer-using-Asymmetric-Cryptography-Algorithm
The Aim of this project is to Transfer Mobile Sensor Data using Asymmetric Cryptography Algorithms Securely
## INTRODUCTION!
- Mobile sensors are playing a vital role in various applications of a normal day life.
- mobile sensors data is used to accommodate various sensors applications including air pressure, temperature, global positioning system (GPS), light intensity,proximity measurement and detect the orientation of device.
- As vulnerability in smart devices may expanded due to the absence of a proper mechanism to secure mobile sensor data against the intruders.
- Therefore, a secure communication of mobile sensor data is necessary , as it has issues with limited memory and low battery .
- Additionally, in a mobile sensor network (MSN), the data communication between sensor nodes and a server data should be secure . 
- In-order to keep up the data security various asymmetric algorithms are proposed  and requires to be employed in securing mobile sensor data transfer among various nodes
- Key size in securing data is an important issue to highlight in mobile sensor data transfer between a smart device and a data storage component. 
- Such key size may affect memory storage and processing power of a mobile device. Therefore, we proposed a secure mobile sensor data transfer protocol called secure sensor protocol (SSP).
- SSP is based on Elliptic Curve Cryptography (ECC), which generates small size key in contrast to conventional asymmetric algorithms like RSA and Diffie Hellman. SSP receive values from light sensor and magnetic flux meter of a smart device.
- SSP encrypts mobile sensor data using ECC and afterwards it stores cipher information in MySQL database to receive remote data access.

- We compared the performance of the ECC with other existing asymmetric cryptography algorithms in terms of secure mobile sensor data transfer based on data encryption and decryption time, key size and encoded data size.
- In-addition, SSP shows better results than other cryptography algorithms in terms of secure mobile sensor data transfer.
- ECC is considered as a most feasible choice for public key cryptography in wireless body area network to deliver more security framework in less computation power in contrast to other cryptographic algorithms

## SSP WORKING

- We use ECC algorithm for key generation, which applies on the mobile sensor (light sensor and magnetic flux meter) data. 
- Firstly, we encrypt sensor data using public key and store the cipher on the cloud. 
- Secondly, a database administrator will get the cipher from the database (data stored on cloud) and a key from smart device which is considered as a source of information that holds data of a particular sensor.

## SYSTEM MODEL

![image](https://user-images.githubusercontent.com/99113503/228792118-06c4e214-0111-47e2-9e49-af060fa3ab2e.png)

## ENCRYPTION                                                                                                      DECRYPTION![image]

![image](https://user-images.githubusercontent.com/99113503/228792708-bbd236f1-1d38-402d-bc6e-4fae7aec55bc.png)       ![image](https://user-images.githubusercontent.com/99113503/228792796-903e7ac0-3695-4a17-9da5-aee42cfd462f.png)





