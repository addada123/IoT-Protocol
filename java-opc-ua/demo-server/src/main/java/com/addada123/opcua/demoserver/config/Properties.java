package com.addada123.opcua.demoserver.config;

import lombok.Getter;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.context.annotation.Configuration;
import org.springframework.context.annotation.PropertySource;

@Getter
@Configuration
@PropertySource("classpath:opcua.properties")
public class Properties {
    @Value("${opcua.server.endpoint.url}")
    private String endpointUrl;
    @Value("${opcua.client.app.name}")
    private String appName;
}