#!/bin/bash

pushd generator
./generateCode.sh
popd

rm -rf sdk/src/azuremarketplace/microsoft/marketplace
mv sdk/src/microsoft/marketplace sdk/src/azuremarketplace/microsoft/marketplace 
rm -rf sdk/src/microsoft
