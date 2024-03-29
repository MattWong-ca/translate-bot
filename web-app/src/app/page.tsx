"use client";
import Image from "next/image";

export default function Home() {
  return (
    <div onClick={() => main("Can you figure out how to make a chatbot?")}>
      Hello world
    </div>
  );
}
import axios from "axios";
import * as dotenv from "dotenv";

// Load environment variables from .env file
dotenv.config({ path: "./.env" }); // Make sure the path is correct

async function main(prompt: string) {
  console.log("Prompt:", prompt);

  try {
    // Construct the request payload
    const payload = {
      question: prompt,
      chat_history: [],
      knowledge_source_id: "<model_id>", // replace with your model id
    };

    // Set the headers
    const headers = {
      "x-api-key": process.env.FLOCK_BOT_API_KEY, // Ensure API key is set in .env
    };

    // Send POST request using axios
    const response = await axios.post(
      `https://rag-chat-ml-backend-prod.flock.io/chat/conversational_rag_chat`,
      payload,
      {
        headers,
      }
    );


    // Output the response data
    console.log(response.data);
  } catch (error) {
    console.error("Error:", error);
  }
}

// Example call to the main function
