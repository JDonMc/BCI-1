
void XXX::send_float (float arg)
{
  // get access to the float as a byte-array:
  byte * data = (byte *) &arg;

  // write the data to the serial
  Serial.write(data, sizeof(arg));
  Serial.println();
  Serial.flush();
}

// haven't tested, not sure what the python requirement is.

