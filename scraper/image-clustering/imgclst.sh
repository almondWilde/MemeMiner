#!/bin/bash
for ((trials = 10; trials > 0; trials--))
	do
		python image_clustering.py
		#mkdir /mnt/d/output/
		sudo mv "/mnt/d/output/" "/mnt/d/cluster-trials/cluster-trial-$trials/"
	done

