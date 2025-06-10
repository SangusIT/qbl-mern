import express from "express";
import db from "../db/connection.js";
import { ObjectId } from "mongodb";

const router = express.Router();

// get all records
router.get("/", async (req, res) => {
    let collection = await db.collection("hunting_grounds");
    let results = await collection.find({}).toArray();
    res.send(results).status(200);
});

// get one record by id
router.get("/:id", async (req, res) => {
    let collection = await db.collection("hunting_grounds");
    // console.log('checking id')
    // console.log(ObjectId.createFromHexString(req.params.id))
    let query = { _id: ObjectId.createFromHexString(req.params.id) };
    let result = await collection.findOne(query);
    if (!result) res.status(404).send("Not found for " + ObjectId.createFromHexString(req.params.id));
    else res.send(result).status(200);
});

// create record
router.post("/", async (req, res) => {
    try {
        let newDocument = {
            name: req.body.name,
            location: req.body.location,
        };
        let collection = await db.collection("hunting_grounds");
        let result = await collection.insertOne(newDocument);
        res.send(result).status(204)
    } catch (err) {
        console.error(err);
        res.status(500).send("Error adding record");
    }
});

// update record by id
router.patch("/:id", async (req, res) => {
    try {
        const query = { _id: ObjectId.createFromHexString(req.params.id) };
        const updates = {
            $set: {
                name: req.body.name,
                location: req.body.location,
            },
        };

        let collection = await db.collection("hunting_grounds");
        let result = await collection.updateOne(query, updates);
        res.send(result).status(200);
    } catch (err) {
        console.error(err);
        res.status(500).send("Error updating record");
    }
});

router.delete("/:id", async (req, res) => {
    try {
        const query = { _id: ObjectId.createFromHexString(req.params.id) };
        const collection = await db.collection("hunting_grounds");
        let result = await collection.deleteOne(query);
        res.send(result).status(200);
    } catch (err) {
        console.error(err);
        res.status(500).send("Error deleting record");
    }
});

export default router;