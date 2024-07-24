# Tech Scams: A One-to-One Analysis with Scammers

This project, developed as part of the King's Undergraduate Research Fellowship, aims to build a software tool that gathers information about tech scams for deep-level analysis. The tool connects users to real scammers through a simulated real-life environment and lets them gain control of the devices.

## Table of Contents

- [Introduction](#introduction)
- [Objective](#objective)
- [Method](#method)
- [Results](#results)
- [Discussion](#discussion)
- [Conclusion](#conclusion)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Introduction

Over the last two decades, the Internet has become an integral part of our lives, with users storing various types of data, including highly confidential information like banking details. However, connecting to the Internet exposes users to numerous threats, one of which is "tech support scams." In these scams, a scammer deceives the user into believing there are issues with their devices and then acts as a support technician to gain control of the victim's computer.

## Objective

The objective of this research is to build a software tool that gathers information about tech scams for a deep-level analysis. This tool connects users to real scammers through a simulated real-life environment and lets them gain control of the devices.

## Method

The research focuses on tech support scamming, where scammers impersonate tech support assistants. Users are tricked into believing their devices have issues and are given contact details to tech support (which are scammers). During the scam, users are asked to download software that gives scammers remote control over their devices.

The tool developed for this research simulates a real-life machine where scammers gain control as instructed by the user. The tool monitors the machine from different views while scammers operate it. Virtual machines (VMs) are used to simulate real-life scenarios and operate in a safe environment, preventing malware damage. Oracle VirtualBox and its API are utilized for this purpose.

## Results

The scam-analysis tool uses VMs to simulate real-life scenarios safely. It creates scenarios where scammers believe they are controlling real devices. Two Python scripts were developed: one to manage the VM with the pyvbox library and another to compare the VM's filesystem before and after scammers operate. The tool produces reports logging all file changes during the scam operation.

## Discussion

Online scams are becoming increasingly sophisticated and dangerous, with scammers accessing users' sensitive information. The tool developed in this research helps identify and classify scams, enabling users to compare potential scam messages with analyzed ones, thus avoiding getting scammed.

## Conclusion

This research provides a tool that can identify and classify scams, helping users avoid falling victim to tech support scams. By comparing suspicious messages with analyzed scams, users can make informed decisions and protect their personal information.

## Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/riccardogugliermini/individual-project.git
