// Auto-generated. Do not edit!

// (in-package uarm.msg)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;

//-----------------------------------------------------------

class Angles {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.servo_1 = null;
      this.servo_2 = null;
      this.servo_3 = null;
      this.servo_4 = null;
    }
    else {
      if (initObj.hasOwnProperty('servo_1')) {
        this.servo_1 = initObj.servo_1
      }
      else {
        this.servo_1 = 0;
      }
      if (initObj.hasOwnProperty('servo_2')) {
        this.servo_2 = initObj.servo_2
      }
      else {
        this.servo_2 = 0;
      }
      if (initObj.hasOwnProperty('servo_3')) {
        this.servo_3 = initObj.servo_3
      }
      else {
        this.servo_3 = 0;
      }
      if (initObj.hasOwnProperty('servo_4')) {
        this.servo_4 = initObj.servo_4
      }
      else {
        this.servo_4 = 0;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type Angles
    // Serialize message field [servo_1]
    bufferOffset = _serializer.uint8(obj.servo_1, buffer, bufferOffset);
    // Serialize message field [servo_2]
    bufferOffset = _serializer.uint8(obj.servo_2, buffer, bufferOffset);
    // Serialize message field [servo_3]
    bufferOffset = _serializer.uint8(obj.servo_3, buffer, bufferOffset);
    // Serialize message field [servo_4]
    bufferOffset = _serializer.uint8(obj.servo_4, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type Angles
    let len;
    let data = new Angles(null);
    // Deserialize message field [servo_1]
    data.servo_1 = _deserializer.uint8(buffer, bufferOffset);
    // Deserialize message field [servo_2]
    data.servo_2 = _deserializer.uint8(buffer, bufferOffset);
    // Deserialize message field [servo_3]
    data.servo_3 = _deserializer.uint8(buffer, bufferOffset);
    // Deserialize message field [servo_4]
    data.servo_4 = _deserializer.uint8(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    return 4;
  }

  static datatype() {
    // Returns string type for a message object
    return 'uarm/Angles';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return 'c365f7c0f52d109b4b516ca588b94bd3';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    uint8 servo_1
    uint8 servo_2
    uint8 servo_3
    uint8 servo_4
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new Angles(null);
    if (msg.servo_1 !== undefined) {
      resolved.servo_1 = msg.servo_1;
    }
    else {
      resolved.servo_1 = 0
    }

    if (msg.servo_2 !== undefined) {
      resolved.servo_2 = msg.servo_2;
    }
    else {
      resolved.servo_2 = 0
    }

    if (msg.servo_3 !== undefined) {
      resolved.servo_3 = msg.servo_3;
    }
    else {
      resolved.servo_3 = 0
    }

    if (msg.servo_4 !== undefined) {
      resolved.servo_4 = msg.servo_4;
    }
    else {
      resolved.servo_4 = 0
    }

    return resolved;
    }
};

module.exports = Angles;
