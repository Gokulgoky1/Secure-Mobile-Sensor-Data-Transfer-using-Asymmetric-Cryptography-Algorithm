

# INTRODUCTION

<span style="color:#000000">Mobile sensors are playing a vital role in various applications of a normal day life\.</span>

<span style="color:#000000">mobile sensors data is used to accommodate various sensors applications including air pressure\, temperature\, global positioning system \(GPS\)\, light intensity\, proximity measurement and detect the orientation of device\.</span>

<span style="color:#000000">As vulnerability in smart devices may expanded due to the absence of a proper mechanism to secure mobile sensor data against the intruders\.</span>

<span style="color:#000000">Therefore\, a secure communication of mobile sensor data is necessary \, as it has issues with limited memory and low battery \.</span>

<span style="color:#000000">Additionally\, in a mobile sensor network \(MSN\)\, the data communication between sensor nodes and a server data should be secure \. </span>

<span style="color:#000000">In\-order to keep up the data security various asymmetric algorithms are proposed  and requires to be employed in securing mobile sensor data transfer among various nodes \. </span>

__Key size in securing data is an important issue to highlight in mobile sensor data transfer between a smart device and a data storage component\. __

__Such key size may affect memory storage and processing power of a mobile device\. Therefore\, we proposed a secure mobile sensor data transfer protocol called __  __secure__  __ __  __sensor protocol \(SSP\)__  __\.__

__SSP is based on __  __Elliptic Curve Cryptography \(ECC\)__  __\, which generates small size key in contrast to conventional asymmetric algorithms like RSA and Diffie Hellman\. SSP receive values from light sensor and magnetic flux meter of a smart device\.__

__SSP encrypts mobile sensor data using ECC and afterwards it stores cipher information in __  __MySQL database__  __ to receive remote data access\.__

<span style="color:#000000">We compared the performance of the ECC with other existing asymmetric cryptography algorithms in terms of secure mobile sensor data transfer based on data </span>  <span style="color:#000000"> __encryption__ </span>  <span style="color:#000000"> and </span>  <span style="color:#000000"> __decryption__ </span>  <span style="color:#000000"> time\, </span>  <span style="color:#000000"> __key size__ </span>  <span style="color:#000000"> and encoded data size\.</span>

<span style="color:#000000">In\-addition\, SSP shows better results than other cryptography algorithms in terms of secure mobile sensor data transfer\.</span>

<span style="color:#000000">ECC is considered as a most feasible choice for public key cryptography in wireless body area network to deliver more security framework in less computation power in contrast to other cryptographic algorithms</span>

# SSP WORKING

__We use ECC algorithm for key generation\, which applies on the mobile sensor \(light sensor and magnetic flux meter\) data\. __

__Firstly\, we encrypt sensor data using public key and store the cipher on the cloud\. __

__Secondly\, a database administrator will get the cipher from the database \(data stored on cloud\) and a key from smart device which is considered as a source of information that holds data of a particular sensor\.__

# SYSTEM MODEL (DIAGRAM)

![](img%5CSecure%20Mobile%20Sensor%20Data%20Transfer%20using%20Asymmetric%20Cryptography0.png)

# ENCRYPTION                                            DECRYPTION

![](img%5CSecure%20Mobile%20Sensor%20Data%20Transfer%20using%20Asymmetric%20Cryptography1.png)

![](img%5CSecure%20Mobile%20Sensor%20Data%20Transfer%20using%20Asymmetric%20Cryptography2.png)

__KEY GENERATION__

__ECC Private key__

__ECC Public Key__

__ENCRYPTION__

__Encrypt the data using ECC public Key__

__DECRYPTION__

__Decrypt the data using __

__ECC private Key__

# ECC ENCRYPTION

![](img%5CSecure%20Mobile%20Sensor%20Data%20Transfer%20using%20Asymmetric%20Cryptography3.png)

* <span style="color:#0D1117">Assume we have a ECC private\-public key pair\. We want to encrypt and decrypt data using these keys\. By definition\, asymmetric encryption works as follows:</span>
  * <span style="color:#0D1117"> if we encrypt data by a private key\, we will be able to decrypt the ciphertext later by the corresponding public key and vice versa</span>

__The process on right side can be directly applied for the RSA cryptosystem\, but not for the ECC\. The elliptic curve cryptography \(ECC\) does not directly provide encryption method\. Instead\, we can design a __  __hybrid encryption scheme__  __ by using the ECDH \(Elliptic Curve Diffie–Hellman\) key exchange scheme to derive a shared secret key for symmetric data encryption and decryption\.__

# HYBRID ENCRYPTION SCHEME-WORKING

![](img%5CSecure%20Mobile%20Sensor%20Data%20Transfer%20using%20Asymmetric%20Cryptography4.png)

![](img%5CSecure%20Mobile%20Sensor%20Data%20Transfer%20using%20Asymmetric%20Cryptography5.png)

Encryption Process

Decryption Process

# ECC-Based Secret Key Derivation (using ECDH)

* __calculateEncryptionKey\(pubKey\) \-\-> \(sharedECCKey\, ciphertextPubKey\)__
  * __Generate ciphertextPrivKey = __  _new random private key_  __\.__
  * __Calculate ciphertextPubKey = ciphertextPrivKey \* G\.__
  * __Calculate the ECDH shared secret:                        sharedECCKey = pubKey \* ciphertextPrivKey\.__
  * __Return both the sharedECCKey \+ ciphertextPubKey\. Use the sharedECCKey for symmetric encryption\. Use the randomly generated ciphertextPubKey to calculate the decryption key later\.__
* __calculateDecryptionKey\(privKey\, ciphertextPubKey\) \-\-> sharedECCKey__
  * __Calculate the the ECDH shared secret: sharedECCKey = ciphertextPubKey \* privKey\.__
  * __Return the sharedECCKey and use it for the decryption\.__

![](img%5CSecure%20Mobile%20Sensor%20Data%20Transfer%20using%20Asymmetric%20Cryptography6.png)

![](img%5CSecure%20Mobile%20Sensor%20Data%20Transfer%20using%20Asymmetric%20Cryptography7.png)

__The above calculations use the same math\, like the ECDH algorithm \(see the __  __[previous section](https://github.com/nakov/Practical-Cryptography-for-Developers-Book/blob/master/asymmetric-key-ciphers/ecdh-key-exchange.md)__  __\)\. Recall that EC points have the following property:__

__\(__  _a_  __ \* G\) \* __  _b_  __ = \(__  _b_  __ \* G\) \* __  _a_

__Now\, assume that __  _a_  __ = privKey\, __  _a_  __ \* G = pubKey\, __  _b_  __ = ciphertextPrivKey\, __  _b_  __ \* G = ciphertextPubKey\.__

__The above equation takes the following form:__

__pubKey \* ciphertextPrivKey = ciphertextPubKey \* privKey = sharedECCKey__

# Implementation

__Record sensor data from your Smartphone and convert it to csv file with the help of __  __sensor logger App__

__The Webpage will run on http://localhost:5000__

# Result and Evaluation

![](img%5CSecure%20Mobile%20Sensor%20Data%20Transfer%20using%20Asymmetric%20Cryptography8.png)

Table 4 shows the key size that is generated by different algorithms which shows that ECC generate much smaller keys in contrast to RSA \. ECC provides an equal level of security with a 163\-bit key while RSA use 1025\-bit key size\.

In Table 5 we can quantify the average time for the encryption and decryption of the sensor data and also the average size of the cipher\. The experiment is executed for 100 estimations of the light intensity sensor\, magnetic field meter and proximity sensor\. The experimental result shows the average sensors time \(second\) and cipher size \(bytes\) of both the algorithms \(ECC and RSA\)\.

![](img%5CSecure%20Mobile%20Sensor%20Data%20Transfer%20using%20Asymmetric%20Cryptography9.png)

__SSP depends on the ECC algorithm we compare our results with the RSA algorithm\. We analyze these two algorithms in terms of the time for encryption and decryption and the cipher size\. __

__The results show that SSP scheme is much better than the RSA in terms of the encryption and decryption time and the cipher size\. __

# CONCLUSION

__A protocol is proposed and called a secure sense protocol \(SSP\)\, to secure data transfer among a smart device \(user\) and a remote database \(cloud data storage\)\.__

__The SSP framework gained more security and diminished the utilization of a memory space of the smart device because the cipher data is stored on the cloud\. __

__We stored both public and private keys on the smart device and cipher of sensor data on the cloud\. Experimental results show that we have obtained higher security\, time efficiency and accurate data transfer of the mobile sensor of a smart device\.__

__However\, the utilization of the ECC in the Android is still ought to be improved for better results\. __

__For future\, optimization of the ECC methods will be implemented to improve size of the key and cipher data__

# FUTURE WORK

__The proposed mechanism in the paper ”Secure Mobile Sensor Data Transfer using Asymmetric Cryptography Algorithms” has a lot of potential for further development and improvement\. __

__One of the future works that can be done is to expand the scope of this mechanism to small IoT devices such as smartwatches and smart bands\. __

__These devices often have limited storage capacity\, and the smaller size of ECC keys compared to RSA keys makes it a good fit for these devices\. By incorporating this mechanism into these small IoT devices\, the sensitive data collected by these devices can be protected more effectively\. __

__Additionally\, further studies can be conducted to compare the performance and security of ECC and RSA algorithms in various scenarios\, and to find ways to optimize the performance of these algorithms to meet the needs of different applications\. __

Overall\, this proposed mechanism has the potential to be a significant contribution to the field of secure mobile sensor data transfer\.

The proposed mechanism can used for improving the security of databases and how it can be integrated with existing database security measures\.

Additionally\, the paper could also explore the performance of the mechanism in terms of speed\, efficiency and scalability\, especially when handling large amounts of data\.

