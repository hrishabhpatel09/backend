import mongoose from "mongoose";
 
 const connectDB = async() => {
    const DB_NAME ="SiH"
    try{
        const connectionInstance=await mongoose.connect(`${process.env.MONGODB_URI}/${DB_NAME}`)
        console.log(`\n MongoDB connected !! DB HOST: ${connectionInstance.connection.host}`);
    } catch(error){
        console.log("\n MongoDB connection error", error);
        process.exit(1)
    }
 }
  ;
 export default connectDB