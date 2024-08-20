import cors from "cors";
import dotenv from "dotenv";
import express from "express";

dotenv.config({
  path: "./src/.env",
});

const app = express();
app.use(
  cors({
    origin: "*",
  })
);

app.get("/", (req, res) => {
  return res.json({ name: "Hrishabh Patel", msg: "Hello World!:😊" });
});

const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
  console.log(`Server listening on port ${PORT}`);
});
