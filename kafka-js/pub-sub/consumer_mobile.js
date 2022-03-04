const { Kafka } = require("kafkajs");

// node consumer.js Logs || Logs2
// const topic_name = process.argv[2] || "Logs2";

createConsumer();

async function createConsumer() {
  try {
    const kafka = new Kafka({
      clientId: "kafka_pub_sub_client",
      brokers: ["192.168.1.3:9092"]
    });

    const consumer = kafka.consumer({
      groupId: "mobile_encoder_consumer_group"
    });

    

    console.log("Consumer'a bağlanılıyor..");
    await consumer.connect();
    console.log("Bağlantı başarılı.");

    // Consumer Subscribe..
    await consumer.subscribe({
      topic: "raw_video_topic",
      fromBeginning: true
    });

    await consumer.run({
      eachMessage: async result => {
        console.log(
          `Gelen Mesaj ${result.message.value}, mobile`
        );
      }
    });
  } catch (error) {
    console.log("Bir Hata Oluştu", error);
  }
}
