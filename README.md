<h1 align="center">
Multipath Network Protocols Lab
</h1>

<p align="center">
  <a href="#about-the-project">About The Project</a> •
  <a href="#getting-started">Getting Started</a> •
  <a href="#usage">Usage</a> •
  <a href="#related">Related</a> •
  <a href="#license">License</a>
</p>


<!-- ABOUT THE PROJECT -->
## About The Project

![](images/topology.svg)


This project is built with Vagrant using Docker as a provider and Ansible for provisioning. 
Once deployed, the proposed virtual environment intends to perform tests on multipath transport protocols such as MPQUIC and MPTCP. 

The proposed test scenarios aim to explore the mechanisms of these protocols, their performance depending on traffic types and conditions, and their use for live video streaming applications.

### Built With

| <!-- --> | <!-- --> |
| -------- | -------- |
| [![VagrantUp.com][Vagrant]][Vagrant-url] | Hashicorp open source software for building portable virtual environments |
| [![Docker.com][Docker]][Vagrant-url] |Open source platform for building, shipping, and running containers
| [![Ansible.com][Ansible]][Ansible-url] | Red Hat open source automation tool
| [![Grafana.com][Grafana]][Grafana-url] | Open source data visualization and monitoring solution
| [![InfluxData.com][InfluxDB]][InfluxDB-url] | Open source time series database (TSDB)


<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->


[Docker]: https://img.shields.io/badge/docker-1F201F?style=for-the-badge&logo=docker
[Docker-url]: https://www.docker.com/
[Vagrant]: https://img.shields.io/badge/vagrant-1868F2?style=for-the-badge&logo=vagrant
[Vagrant-url]: https://www.vagrantup.com/
[Ansible]: https://img.shields.io/badge/ansible-000000?style=for-the-badge&logo=ansible
[Ansible-url]: https://www.ansible.com/
[Grafana]: https://img.shields.io/badge/grafana-1D1D1D?style=for-the-badge&logo=grafana
[Grafana-url]: https://grafana.com/
[InfluxDB]: https://img.shields.io/badge/influxdb-020A43?style=for-the-badge&logo=influxdb
[InfluxDB-url]: https://www.influxdata.com/