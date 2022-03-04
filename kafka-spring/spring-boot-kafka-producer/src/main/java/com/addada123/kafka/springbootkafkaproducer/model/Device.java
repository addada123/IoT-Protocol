package com.addada123.kafka.springbootkafkaproducer.model;

public class Device {
    private String temp;

    public Device(String temp) {
        this.temp = temp;
    }

    void setTemp(String temp) {
        this.temp = temp;
    }

    String getTemp() {
        return temp;
    }
}
