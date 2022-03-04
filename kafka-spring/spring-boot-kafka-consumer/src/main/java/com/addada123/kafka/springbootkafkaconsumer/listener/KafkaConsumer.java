package com.addada123.kafka.springbootkafkaconsumer.listener;

import com.addada123.kafka.springbootkafkaconsumer.model.User;

import org.springframework.kafka.annotation.KafkaListener;
import org.springframework.stereotype.Service;

@Service
public class KafkaConsumer {
    @KafkaListener(topics = "test", groupId = "group_id", containerFactory = "KafkaConfiguration")
    public void consume(User user) {
        System.out.println("Consumed message: " + user);
    }
}
