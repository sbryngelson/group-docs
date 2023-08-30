# Computers

* PACE Phoenix
    * User guide [here](https://docs.pace.gatech.edu/phoenix_cluster/gettingstarted_phnx/)
    * Purpose: All-purpose campus resource of CPU and GPU jobs with a variety of hardware. 
    * "Rules": Use the `embers` queue type to use idle nodes at zero cost.
    * Get access by: emailing pace-support@oit.gatech.edu requesting access under project p-sbryngelson3 with PI Spencer Bryngelson. They will send me an email to confirm your membership.

* Rogues Gallery 
    * User guide [here](https://gt-crnch-rg.readthedocs.io/en/main/)
    * Purpose: Use of brand-new, forward looking, or weird hardware. At time of writing, including NV H100 server, AMD MI200-series GPU server, Bluefield-2/3 SmartNICs, RISC-V and ARM CPUs, etc.
    * "Rules": Few rules, just follow guidelines in documentation. No limitations on hardware access/node hours.
    * Get access by: Using [this link](https://crnch-rg.cc.gatech.edu/request-rogues-gallery-access/)

* Wingtip-gpu3
    * User guide [here](https://github.gatech.edu/cse-computing/compute-resources/blob/main/docs/systems/wingtip-gpu.md)
    * Purpose: Small (but possibly very long) GPU jobs, hosts 5x NV A100-80GB at the moment
    * "Rules": No scheduler on this machine so be mindful of others use of it.
    * Get access by: Emailing [Will Powell](will.powell@cc.gatech.edu), cc me.

* ACCESS-CI computers
    * These are a set of university supercomputers, listed [here](https://access-ci.org/resource-providers/). Each has its own user guide. We have access to NCSA Delta and PSC Bridges2 at time of writing, but can change to others as needed.
    * Purpose: All-purpose resources for CPU and GPU simulation. 
    * "Rules": Be mindful of node hours available. Queue times might be long.
    * Get access by
        * Creating an account [here](https://identity.access-ci.org/new-user.html)
        * Then, message Spencer on Slack with your username

* OLCF Summit/Frontier/Wombat/Crusher/etc.
    * Purpose
        * Summit: Very large-scale GPU simulation (up to 24K V100 GPUs), going offline near end of 2023.
        * Frontier: Very large-scale GPU simulation on AMD MI250X GPUs.
        * Crusher: Testbed for AMD GPU use, has latest Cray compilers and ROCm.
        * Wombat: Testbed for next-gen HPC platforms, including ARM nodes and soon next-generation NVIDIA nodes (GraceHopper).
    * "Rules": Ask Spencer before running any jobs that use a very large number of node hours
    * Get access by
        * Creating an account by following [these instructions](https://docs.olcf.ornl.gov/accounts/accounts_and_projects.html#applying-for-a-user-account)
        * The account/allocation number is CFD154.
