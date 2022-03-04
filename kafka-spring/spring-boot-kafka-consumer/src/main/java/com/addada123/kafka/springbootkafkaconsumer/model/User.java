package com.addada123.kafka.springbootkafkaconsumer.model;

public class User {
    private Integer temp;
    private Integer height;
    private String time;

    public User(Integer temp, Integer height, String time) {
        this.temp = temp;
        this.height = height;
        this.time = time;
    }

    public Integer getTemp() {
        return temp;
    }

    public void setTemp(Integer temp) {
        this.temp = temp;
    }

    public Integer getHeight() {
        return height;
    }

    public void set(Integer height) {
        this.height = height;
    }

    public String getTime() {
        return time;
    }

}
