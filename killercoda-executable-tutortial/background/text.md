Testcontainers uses docker internally to run the various services, which makes it possible to run a lot of services since all you need is the docker image. It does this by providing a programmatic API (for many programming languages, one of them is Python) that can be used to run any docker image, retrieve container information, stop the container and get the container mapped port because Testcontainers will automatically map the containers port onto random ports that are available on the host machine so that even if one had these services running locally it would not interfere. 

This comes in two flavours the first one is known as the GenericContainer here one supplies the docker image and the configuration and such for the service and optionally define when the service is considered up and running this can be achieved by waiting for X amount of seconds or waiting for a specific Log message to be outputted for instance. 

The second flavour is what Testcontainers calls modules these are a wide range of commonly used services which have already been configured and can be run without any boilerplate but also make it easier to access specific relevant service parameters. Modules are a higher-level abstraction of the GenericContainer so they still use the GenericContainer internally. 

To recap Testcontainers when used in testing does the following things it will automatically start the container and make sure they are in a desired state before testing occurs, then the tests will run using these containerized services. Lastly, after execution has finished Testcontainers will destroy and remove the containers. This is visualised below 

![test-workflow](../../killercoda-executable-tutortial/assets/testcontainers-flow.png)
