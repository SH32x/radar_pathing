The src directory contains the full implementation of the project.

Note that files in src are not intended to be standalone and are meant to integrate the live radar/vehicle data, meaning that these files cannot be run without the hardware setup.

Because of this, most of the design of the components should be done in the development directory, where they can be tested using stubs.
