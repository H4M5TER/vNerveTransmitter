// source: vNerve/vdb/vdb.proto
/**
 * @fileoverview
 * @enhanceable
 * @suppress {messageConventions} JS Compiler reports an error if a variable or
 *     field starts with 'MSG_' and isn't a translatable message.
 * @public
 */
// GENERATED CODE -- DO NOT EDIT!

var jspb = require('google-protobuf');
var goog = jspb;
var global = Function('return this')();

goog.exportSymbol('proto.vNerve.vdb.Account', null, global);
goog.exportSymbol('proto.vNerve.vdb.AccountPlatform', null, global);
goog.exportSymbol('proto.vNerve.vdb.AccountType', null, global);
goog.exportSymbol('proto.vNerve.vdb.GetVtbsRequest', null, global);
goog.exportSymbol('proto.vNerve.vdb.Vtuber', null, global);
goog.exportSymbol('proto.vNerve.vdb.VtuberCollection', null, global);
goog.exportSymbol('proto.vNerve.vdb.VtuberType', null, global);
/**
 * Generated by JsPbCodeGenerator.
 * @param {Array=} opt_data Optional initial data array, typically from a
 * server response, or constructed directly in Javascript. The array is used
 * in place and becomes part of the constructed object. It is not cloned.
 * If no data is provided, the constructed object will be empty, but still
 * valid.
 * @extends {jspb.Message}
 * @constructor
 */
proto.vNerve.vdb.GetVtbsRequest = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.vNerve.vdb.GetVtbsRequest, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  /**
   * @public
   * @override
   */
  proto.vNerve.vdb.GetVtbsRequest.displayName = 'proto.vNerve.vdb.GetVtbsRequest';
}
/**
 * Generated by JsPbCodeGenerator.
 * @param {Array=} opt_data Optional initial data array, typically from a
 * server response, or constructed directly in Javascript. The array is used
 * in place and becomes part of the constructed object. It is not cloned.
 * If no data is provided, the constructed object will be empty, but still
 * valid.
 * @extends {jspb.Message}
 * @constructor
 */
proto.vNerve.vdb.VtuberCollection = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, proto.vNerve.vdb.VtuberCollection.repeatedFields_, null);
};
goog.inherits(proto.vNerve.vdb.VtuberCollection, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  /**
   * @public
   * @override
   */
  proto.vNerve.vdb.VtuberCollection.displayName = 'proto.vNerve.vdb.VtuberCollection';
}
/**
 * Generated by JsPbCodeGenerator.
 * @param {Array=} opt_data Optional initial data array, typically from a
 * server response, or constructed directly in Javascript. The array is used
 * in place and becomes part of the constructed object. It is not cloned.
 * If no data is provided, the constructed object will be empty, but still
 * valid.
 * @extends {jspb.Message}
 * @constructor
 */
proto.vNerve.vdb.Vtuber = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, proto.vNerve.vdb.Vtuber.repeatedFields_, null);
};
goog.inherits(proto.vNerve.vdb.Vtuber, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  /**
   * @public
   * @override
   */
  proto.vNerve.vdb.Vtuber.displayName = 'proto.vNerve.vdb.Vtuber';
}
/**
 * Generated by JsPbCodeGenerator.
 * @param {Array=} opt_data Optional initial data array, typically from a
 * server response, or constructed directly in Javascript. The array is used
 * in place and becomes part of the constructed object. It is not cloned.
 * If no data is provided, the constructed object will be empty, but still
 * valid.
 * @extends {jspb.Message}
 * @constructor
 */
proto.vNerve.vdb.Account = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, proto.vNerve.vdb.Account.repeatedFields_, null);
};
goog.inherits(proto.vNerve.vdb.Account, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  /**
   * @public
   * @override
   */
  proto.vNerve.vdb.Account.displayName = 'proto.vNerve.vdb.Account';
}



if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * Optional fields that are not set will be set to undefined.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     net/proto2/compiler/js/internal/generator.cc#kKeyword.
 * @param {boolean=} opt_includeInstance Deprecated. whether to include the
 *     JSPB instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @return {!Object}
 */
proto.vNerve.vdb.GetVtbsRequest.prototype.toObject = function(opt_includeInstance) {
  return proto.vNerve.vdb.GetVtbsRequest.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Deprecated. Whether to include
 *     the JSPB instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.vNerve.vdb.GetVtbsRequest} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.vNerve.vdb.GetVtbsRequest.toObject = function(includeInstance, msg) {
  var f, obj = {

  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.vNerve.vdb.GetVtbsRequest}
 */
proto.vNerve.vdb.GetVtbsRequest.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.vNerve.vdb.GetVtbsRequest;
  return proto.vNerve.vdb.GetVtbsRequest.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.vNerve.vdb.GetVtbsRequest} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.vNerve.vdb.GetVtbsRequest}
 */
proto.vNerve.vdb.GetVtbsRequest.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    default:
      reader.skipField();
      break;
    }
  }
  return msg;
};


/**
 * Serializes the message to binary data (in protobuf wire format).
 * @return {!Uint8Array}
 */
proto.vNerve.vdb.GetVtbsRequest.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.vNerve.vdb.GetVtbsRequest.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.vNerve.vdb.GetVtbsRequest} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.vNerve.vdb.GetVtbsRequest.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
};



/**
 * List of repeated fields within this message type.
 * @private {!Array<number>}
 * @const
 */
proto.vNerve.vdb.VtuberCollection.repeatedFields_ = [1];



if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * Optional fields that are not set will be set to undefined.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     net/proto2/compiler/js/internal/generator.cc#kKeyword.
 * @param {boolean=} opt_includeInstance Deprecated. whether to include the
 *     JSPB instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @return {!Object}
 */
proto.vNerve.vdb.VtuberCollection.prototype.toObject = function(opt_includeInstance) {
  return proto.vNerve.vdb.VtuberCollection.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Deprecated. Whether to include
 *     the JSPB instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.vNerve.vdb.VtuberCollection} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.vNerve.vdb.VtuberCollection.toObject = function(includeInstance, msg) {
  var f, obj = {
    vtubersList: jspb.Message.toObjectList(msg.getVtubersList(),
    proto.vNerve.vdb.Vtuber.toObject, includeInstance)
  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.vNerve.vdb.VtuberCollection}
 */
proto.vNerve.vdb.VtuberCollection.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.vNerve.vdb.VtuberCollection;
  return proto.vNerve.vdb.VtuberCollection.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.vNerve.vdb.VtuberCollection} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.vNerve.vdb.VtuberCollection}
 */
proto.vNerve.vdb.VtuberCollection.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = new proto.vNerve.vdb.Vtuber;
      reader.readMessage(value,proto.vNerve.vdb.Vtuber.deserializeBinaryFromReader);
      msg.addVtubers(value);
      break;
    default:
      reader.skipField();
      break;
    }
  }
  return msg;
};


/**
 * Serializes the message to binary data (in protobuf wire format).
 * @return {!Uint8Array}
 */
proto.vNerve.vdb.VtuberCollection.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.vNerve.vdb.VtuberCollection.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.vNerve.vdb.VtuberCollection} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.vNerve.vdb.VtuberCollection.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getVtubersList();
  if (f.length > 0) {
    writer.writeRepeatedMessage(
      1,
      f,
      proto.vNerve.vdb.Vtuber.serializeBinaryToWriter
    );
  }
};


/**
 * repeated Vtuber vtubers = 1;
 * @return {!Array<!proto.vNerve.vdb.Vtuber>}
 */
proto.vNerve.vdb.VtuberCollection.prototype.getVtubersList = function() {
  return /** @type{!Array<!proto.vNerve.vdb.Vtuber>} */ (
    jspb.Message.getRepeatedWrapperField(this, proto.vNerve.vdb.Vtuber, 1));
};


/**
 * @param {!Array<!proto.vNerve.vdb.Vtuber>} value
 * @return {!proto.vNerve.vdb.VtuberCollection} returns this
*/
proto.vNerve.vdb.VtuberCollection.prototype.setVtubersList = function(value) {
  return jspb.Message.setRepeatedWrapperField(this, 1, value);
};


/**
 * @param {!proto.vNerve.vdb.Vtuber=} opt_value
 * @param {number=} opt_index
 * @return {!proto.vNerve.vdb.Vtuber}
 */
proto.vNerve.vdb.VtuberCollection.prototype.addVtubers = function(opt_value, opt_index) {
  return jspb.Message.addToRepeatedWrapperField(this, 1, opt_value, proto.vNerve.vdb.Vtuber, opt_index);
};


/**
 * Clears the list making it empty but non-null.
 * @return {!proto.vNerve.vdb.VtuberCollection} returns this
 */
proto.vNerve.vdb.VtuberCollection.prototype.clearVtubersList = function() {
  return this.setVtubersList([]);
};



/**
 * List of repeated fields within this message type.
 * @private {!Array<number>}
 * @const
 */
proto.vNerve.vdb.Vtuber.repeatedFields_ = [4];



if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * Optional fields that are not set will be set to undefined.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     net/proto2/compiler/js/internal/generator.cc#kKeyword.
 * @param {boolean=} opt_includeInstance Deprecated. whether to include the
 *     JSPB instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @return {!Object}
 */
proto.vNerve.vdb.Vtuber.prototype.toObject = function(opt_includeInstance) {
  return proto.vNerve.vdb.Vtuber.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Deprecated. Whether to include
 *     the JSPB instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.vNerve.vdb.Vtuber} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.vNerve.vdb.Vtuber.toObject = function(includeInstance, msg) {
  var f, obj = {
    uuid: jspb.Message.getFieldWithDefault(msg, 1, ""),
    type: jspb.Message.getFieldWithDefault(msg, 2, 0),
    bot: jspb.Message.getBooleanFieldWithDefault(msg, 3, false),
    accountsList: jspb.Message.toObjectList(msg.getAccountsList(),
    proto.vNerve.vdb.Account.toObject, includeInstance),
    groupUuid: jspb.Message.getFieldWithDefault(msg, 5, ""),
    model2d: jspb.Message.getBooleanFieldWithDefault(msg, 6, false),
    model3d: jspb.Message.getBooleanFieldWithDefault(msg, 7, false),
    model2dArtistUuid: jspb.Message.getFieldWithDefault(msg, 8, ""),
    model3dArtistUuid: jspb.Message.getFieldWithDefault(msg, 9, "")
  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.vNerve.vdb.Vtuber}
 */
proto.vNerve.vdb.Vtuber.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.vNerve.vdb.Vtuber;
  return proto.vNerve.vdb.Vtuber.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.vNerve.vdb.Vtuber} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.vNerve.vdb.Vtuber}
 */
proto.vNerve.vdb.Vtuber.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = /** @type {string} */ (reader.readString());
      msg.setUuid(value);
      break;
    case 2:
      var value = /** @type {!proto.vNerve.vdb.VtuberType} */ (reader.readEnum());
      msg.setType(value);
      break;
    case 3:
      var value = /** @type {boolean} */ (reader.readBool());
      msg.setBot(value);
      break;
    case 4:
      var value = new proto.vNerve.vdb.Account;
      reader.readMessage(value,proto.vNerve.vdb.Account.deserializeBinaryFromReader);
      msg.addAccounts(value);
      break;
    case 5:
      var value = /** @type {string} */ (reader.readString());
      msg.setGroupUuid(value);
      break;
    case 6:
      var value = /** @type {boolean} */ (reader.readBool());
      msg.setModel2d(value);
      break;
    case 7:
      var value = /** @type {boolean} */ (reader.readBool());
      msg.setModel3d(value);
      break;
    case 8:
      var value = /** @type {string} */ (reader.readString());
      msg.setModel2dArtistUuid(value);
      break;
    case 9:
      var value = /** @type {string} */ (reader.readString());
      msg.setModel3dArtistUuid(value);
      break;
    default:
      reader.skipField();
      break;
    }
  }
  return msg;
};


/**
 * Serializes the message to binary data (in protobuf wire format).
 * @return {!Uint8Array}
 */
proto.vNerve.vdb.Vtuber.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.vNerve.vdb.Vtuber.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.vNerve.vdb.Vtuber} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.vNerve.vdb.Vtuber.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getUuid();
  if (f.length > 0) {
    writer.writeString(
      1,
      f
    );
  }
  f = message.getType();
  if (f !== 0.0) {
    writer.writeEnum(
      2,
      f
    );
  }
  f = message.getBot();
  if (f) {
    writer.writeBool(
      3,
      f
    );
  }
  f = message.getAccountsList();
  if (f.length > 0) {
    writer.writeRepeatedMessage(
      4,
      f,
      proto.vNerve.vdb.Account.serializeBinaryToWriter
    );
  }
  f = message.getGroupUuid();
  if (f.length > 0) {
    writer.writeString(
      5,
      f
    );
  }
  f = message.getModel2d();
  if (f) {
    writer.writeBool(
      6,
      f
    );
  }
  f = message.getModel3d();
  if (f) {
    writer.writeBool(
      7,
      f
    );
  }
  f = message.getModel2dArtistUuid();
  if (f.length > 0) {
    writer.writeString(
      8,
      f
    );
  }
  f = message.getModel3dArtistUuid();
  if (f.length > 0) {
    writer.writeString(
      9,
      f
    );
  }
};


/**
 * optional string uuid = 1;
 * @return {string}
 */
proto.vNerve.vdb.Vtuber.prototype.getUuid = function() {
  return /** @type {string} */ (jspb.Message.getFieldWithDefault(this, 1, ""));
};


/**
 * @param {string} value
 * @return {!proto.vNerve.vdb.Vtuber} returns this
 */
proto.vNerve.vdb.Vtuber.prototype.setUuid = function(value) {
  return jspb.Message.setProto3StringField(this, 1, value);
};


/**
 * optional VtuberType type = 2;
 * @return {!proto.vNerve.vdb.VtuberType}
 */
proto.vNerve.vdb.Vtuber.prototype.getType = function() {
  return /** @type {!proto.vNerve.vdb.VtuberType} */ (jspb.Message.getFieldWithDefault(this, 2, 0));
};


/**
 * @param {!proto.vNerve.vdb.VtuberType} value
 * @return {!proto.vNerve.vdb.Vtuber} returns this
 */
proto.vNerve.vdb.Vtuber.prototype.setType = function(value) {
  return jspb.Message.setProto3EnumField(this, 2, value);
};


/**
 * optional bool bot = 3;
 * @return {boolean}
 */
proto.vNerve.vdb.Vtuber.prototype.getBot = function() {
  return /** @type {boolean} */ (jspb.Message.getBooleanFieldWithDefault(this, 3, false));
};


/**
 * @param {boolean} value
 * @return {!proto.vNerve.vdb.Vtuber} returns this
 */
proto.vNerve.vdb.Vtuber.prototype.setBot = function(value) {
  return jspb.Message.setProto3BooleanField(this, 3, value);
};


/**
 * repeated Account accounts = 4;
 * @return {!Array<!proto.vNerve.vdb.Account>}
 */
proto.vNerve.vdb.Vtuber.prototype.getAccountsList = function() {
  return /** @type{!Array<!proto.vNerve.vdb.Account>} */ (
    jspb.Message.getRepeatedWrapperField(this, proto.vNerve.vdb.Account, 4));
};


/**
 * @param {!Array<!proto.vNerve.vdb.Account>} value
 * @return {!proto.vNerve.vdb.Vtuber} returns this
*/
proto.vNerve.vdb.Vtuber.prototype.setAccountsList = function(value) {
  return jspb.Message.setRepeatedWrapperField(this, 4, value);
};


/**
 * @param {!proto.vNerve.vdb.Account=} opt_value
 * @param {number=} opt_index
 * @return {!proto.vNerve.vdb.Account}
 */
proto.vNerve.vdb.Vtuber.prototype.addAccounts = function(opt_value, opt_index) {
  return jspb.Message.addToRepeatedWrapperField(this, 4, opt_value, proto.vNerve.vdb.Account, opt_index);
};


/**
 * Clears the list making it empty but non-null.
 * @return {!proto.vNerve.vdb.Vtuber} returns this
 */
proto.vNerve.vdb.Vtuber.prototype.clearAccountsList = function() {
  return this.setAccountsList([]);
};


/**
 * optional string group_uuid = 5;
 * @return {string}
 */
proto.vNerve.vdb.Vtuber.prototype.getGroupUuid = function() {
  return /** @type {string} */ (jspb.Message.getFieldWithDefault(this, 5, ""));
};


/**
 * @param {string} value
 * @return {!proto.vNerve.vdb.Vtuber} returns this
 */
proto.vNerve.vdb.Vtuber.prototype.setGroupUuid = function(value) {
  return jspb.Message.setProto3StringField(this, 5, value);
};


/**
 * optional bool model_2d = 6;
 * @return {boolean}
 */
proto.vNerve.vdb.Vtuber.prototype.getModel2d = function() {
  return /** @type {boolean} */ (jspb.Message.getBooleanFieldWithDefault(this, 6, false));
};


/**
 * @param {boolean} value
 * @return {!proto.vNerve.vdb.Vtuber} returns this
 */
proto.vNerve.vdb.Vtuber.prototype.setModel2d = function(value) {
  return jspb.Message.setProto3BooleanField(this, 6, value);
};


/**
 * optional bool model_3d = 7;
 * @return {boolean}
 */
proto.vNerve.vdb.Vtuber.prototype.getModel3d = function() {
  return /** @type {boolean} */ (jspb.Message.getBooleanFieldWithDefault(this, 7, false));
};


/**
 * @param {boolean} value
 * @return {!proto.vNerve.vdb.Vtuber} returns this
 */
proto.vNerve.vdb.Vtuber.prototype.setModel3d = function(value) {
  return jspb.Message.setProto3BooleanField(this, 7, value);
};


/**
 * optional string model_2d_artist_uuid = 8;
 * @return {string}
 */
proto.vNerve.vdb.Vtuber.prototype.getModel2dArtistUuid = function() {
  return /** @type {string} */ (jspb.Message.getFieldWithDefault(this, 8, ""));
};


/**
 * @param {string} value
 * @return {!proto.vNerve.vdb.Vtuber} returns this
 */
proto.vNerve.vdb.Vtuber.prototype.setModel2dArtistUuid = function(value) {
  return jspb.Message.setProto3StringField(this, 8, value);
};


/**
 * optional string model_3d_artist_uuid = 9;
 * @return {string}
 */
proto.vNerve.vdb.Vtuber.prototype.getModel3dArtistUuid = function() {
  return /** @type {string} */ (jspb.Message.getFieldWithDefault(this, 9, ""));
};


/**
 * @param {string} value
 * @return {!proto.vNerve.vdb.Vtuber} returns this
 */
proto.vNerve.vdb.Vtuber.prototype.setModel3dArtistUuid = function(value) {
  return jspb.Message.setProto3StringField(this, 9, value);
};



/**
 * List of repeated fields within this message type.
 * @private {!Array<number>}
 * @const
 */
proto.vNerve.vdb.Account.repeatedFields_ = [4];



if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * Optional fields that are not set will be set to undefined.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     net/proto2/compiler/js/internal/generator.cc#kKeyword.
 * @param {boolean=} opt_includeInstance Deprecated. whether to include the
 *     JSPB instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @return {!Object}
 */
proto.vNerve.vdb.Account.prototype.toObject = function(opt_includeInstance) {
  return proto.vNerve.vdb.Account.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Deprecated. Whether to include
 *     the JSPB instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.vNerve.vdb.Account} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.vNerve.vdb.Account.toObject = function(includeInstance, msg) {
  var f, obj = {
    id: jspb.Message.getFieldWithDefault(msg, 1, ""),
    accountType: jspb.Message.getFieldWithDefault(msg, 2, 0),
    accountPlatform: jspb.Message.getFieldWithDefault(msg, 3, 0),
    extraList: (f = jspb.Message.getRepeatedField(msg, 4)) == null ? undefined : f,
    name: jspb.Message.getFieldWithDefault(msg, 5, ""),
    nameTranslationMap: (f = msg.getNameTranslationMap()) ? f.toObject(includeInstance, undefined) : []
  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.vNerve.vdb.Account}
 */
proto.vNerve.vdb.Account.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.vNerve.vdb.Account;
  return proto.vNerve.vdb.Account.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.vNerve.vdb.Account} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.vNerve.vdb.Account}
 */
proto.vNerve.vdb.Account.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = /** @type {string} */ (reader.readString());
      msg.setId(value);
      break;
    case 2:
      var value = /** @type {!proto.vNerve.vdb.AccountType} */ (reader.readEnum());
      msg.setAccountType(value);
      break;
    case 3:
      var value = /** @type {!proto.vNerve.vdb.AccountPlatform} */ (reader.readEnum());
      msg.setAccountPlatform(value);
      break;
    case 4:
      var value = /** @type {string} */ (reader.readString());
      msg.addExtra(value);
      break;
    case 5:
      var value = /** @type {string} */ (reader.readString());
      msg.setName(value);
      break;
    case 6:
      var value = msg.getNameTranslationMap();
      reader.readMessage(value, function(message, reader) {
        jspb.Map.deserializeBinary(message, reader, jspb.BinaryReader.prototype.readString, jspb.BinaryReader.prototype.readString, null, "", "");
         });
      break;
    default:
      reader.skipField();
      break;
    }
  }
  return msg;
};


/**
 * Serializes the message to binary data (in protobuf wire format).
 * @return {!Uint8Array}
 */
proto.vNerve.vdb.Account.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.vNerve.vdb.Account.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.vNerve.vdb.Account} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.vNerve.vdb.Account.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getId();
  if (f.length > 0) {
    writer.writeString(
      1,
      f
    );
  }
  f = message.getAccountType();
  if (f !== 0.0) {
    writer.writeEnum(
      2,
      f
    );
  }
  f = message.getAccountPlatform();
  if (f !== 0.0) {
    writer.writeEnum(
      3,
      f
    );
  }
  f = message.getExtraList();
  if (f.length > 0) {
    writer.writeRepeatedString(
      4,
      f
    );
  }
  f = message.getName();
  if (f.length > 0) {
    writer.writeString(
      5,
      f
    );
  }
  f = message.getNameTranslationMap(true);
  if (f && f.getLength() > 0) {
    f.serializeBinary(6, writer, jspb.BinaryWriter.prototype.writeString, jspb.BinaryWriter.prototype.writeString);
  }
};


/**
 * optional string id = 1;
 * @return {string}
 */
proto.vNerve.vdb.Account.prototype.getId = function() {
  return /** @type {string} */ (jspb.Message.getFieldWithDefault(this, 1, ""));
};


/**
 * @param {string} value
 * @return {!proto.vNerve.vdb.Account} returns this
 */
proto.vNerve.vdb.Account.prototype.setId = function(value) {
  return jspb.Message.setProto3StringField(this, 1, value);
};


/**
 * optional AccountType account_type = 2;
 * @return {!proto.vNerve.vdb.AccountType}
 */
proto.vNerve.vdb.Account.prototype.getAccountType = function() {
  return /** @type {!proto.vNerve.vdb.AccountType} */ (jspb.Message.getFieldWithDefault(this, 2, 0));
};


/**
 * @param {!proto.vNerve.vdb.AccountType} value
 * @return {!proto.vNerve.vdb.Account} returns this
 */
proto.vNerve.vdb.Account.prototype.setAccountType = function(value) {
  return jspb.Message.setProto3EnumField(this, 2, value);
};


/**
 * optional AccountPlatform account_platform = 3;
 * @return {!proto.vNerve.vdb.AccountPlatform}
 */
proto.vNerve.vdb.Account.prototype.getAccountPlatform = function() {
  return /** @type {!proto.vNerve.vdb.AccountPlatform} */ (jspb.Message.getFieldWithDefault(this, 3, 0));
};


/**
 * @param {!proto.vNerve.vdb.AccountPlatform} value
 * @return {!proto.vNerve.vdb.Account} returns this
 */
proto.vNerve.vdb.Account.prototype.setAccountPlatform = function(value) {
  return jspb.Message.setProto3EnumField(this, 3, value);
};


/**
 * repeated string extra = 4;
 * @return {!Array<string>}
 */
proto.vNerve.vdb.Account.prototype.getExtraList = function() {
  return /** @type {!Array<string>} */ (jspb.Message.getRepeatedField(this, 4));
};


/**
 * @param {!Array<string>} value
 * @return {!proto.vNerve.vdb.Account} returns this
 */
proto.vNerve.vdb.Account.prototype.setExtraList = function(value) {
  return jspb.Message.setField(this, 4, value || []);
};


/**
 * @param {string} value
 * @param {number=} opt_index
 * @return {!proto.vNerve.vdb.Account} returns this
 */
proto.vNerve.vdb.Account.prototype.addExtra = function(value, opt_index) {
  return jspb.Message.addToRepeatedField(this, 4, value, opt_index);
};


/**
 * Clears the list making it empty but non-null.
 * @return {!proto.vNerve.vdb.Account} returns this
 */
proto.vNerve.vdb.Account.prototype.clearExtraList = function() {
  return this.setExtraList([]);
};


/**
 * optional string name = 5;
 * @return {string}
 */
proto.vNerve.vdb.Account.prototype.getName = function() {
  return /** @type {string} */ (jspb.Message.getFieldWithDefault(this, 5, ""));
};


/**
 * @param {string} value
 * @return {!proto.vNerve.vdb.Account} returns this
 */
proto.vNerve.vdb.Account.prototype.setName = function(value) {
  return jspb.Message.setProto3StringField(this, 5, value);
};


/**
 * map<string, string> name_translation = 6;
 * @param {boolean=} opt_noLazyCreate Do not create the map if
 * empty, instead returning `undefined`
 * @return {!jspb.Map<string,string>}
 */
proto.vNerve.vdb.Account.prototype.getNameTranslationMap = function(opt_noLazyCreate) {
  return /** @type {!jspb.Map<string,string>} */ (
      jspb.Message.getMapField(this, 6, opt_noLazyCreate,
      null));
};


/**
 * Clears values from the map. The map will be non-null.
 * @return {!proto.vNerve.vdb.Account} returns this
 */
proto.vNerve.vdb.Account.prototype.clearNameTranslationMap = function() {
  this.getNameTranslationMap().clear();
  return this;};


/**
 * @enum {number}
 */
proto.vNerve.vdb.VtuberType = {
  UNKNOWN_VTUBER_TYPE: 0,
  VTUBER: 1,
  GROUP: 2,
  FAN: 3
};

/**
 * @enum {number}
 */
proto.vNerve.vdb.AccountType = {
  UNKNOWN_ACCOUNT_TYPE: 0,
  OFFICIAL: 1,
  RELAY: 2
};

/**
 * @enum {number}
 */
proto.vNerve.vdb.AccountPlatform = {
  UNKNOWN_PLATFORM: 0,
  BILIBILI: 1,
  TWITTER: 2,
  YOUTUBE: 3,
  USERLOCAL: 4,
  PEING: 5,
  MARSHMALLOW: 6,
  PIXIV: 7,
  WEIBO: 8,
  BOOTH: 9,
  AFDIAN: 10,
  WEB: 11,
  EMAIL: 12,
  INSTAGRAM: 13,
  POPIASK: 14,
  AMAZON_CO_JP: 15,
  TWITCH: 16,
  NICONICO: 17,
  FACEBOOK: 18,
  TEESPRING: 19,
  PATREON: 20,
  JVCMUSIC: 21,
  CI_EN: 22,
  GITHUB: 23,
  LINE: 24,
  TIKTOK: 25,
  FANTIA: 26,
  SHOWROOM: 27,
  TELEGRAM: 28
};

goog.object.extend(exports, proto.vNerve.vdb);
