import cors from "cors";
import dotenv from "dotenv";
import express from "express";
import { upload } from "./middlewares/multer.middleware.js";
import connectDB from "./db/db.js";
import { Server } from "socket.io";
import {createServer} from 'http'
import ApiResponse from './utils/apiResonse.js'

dotenv.config({
  path: "./src/.env",
});
let response = null
const app = express();
const server = createServer(app);
const io = new Server(server, {
  cors: {
    origin: '*', // Adjust this as needed for security
    methods: ['GET', 'POST']
  }
});

app.use(
  cors({
    origin: "*",
  })
);

app.get("/", (req, res) => {
  return res.json({ name: "Hrishabh Patel", msg: "Hello World!:😊" });
});


app.post('/video',upload.single('video'),(req,res)=>{
  const file = req.file;
  if(!file)return res.json(new ApiResponse('Please provide a video',{data: null}, false))
    io.emit('process_video',file.filename)
  console.log('hi')

  setTimeout(()=>{
    return res.json(new ApiResponse('Sucess',{},true))
  },5000)
})


io.on('connection',(socket)=>{
  socket.on('data',(data)=>{
    response = data
  })
})

const PORT = process.env.PORT || 3000;
server.listen(PORT, async() => {
  await connectDB();
  console.log(`Server listening on port ${PORT}`);
});
