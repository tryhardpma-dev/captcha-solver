# model.py

import torch
import torch.nn as nn
import torch.nn.functional as F

class CaptchaCNN( nn.Module ):
    def __init__( self ) :
        super().__init__()
        self.conv1 = nn.Conv2d( 1, 32, 3, padding = 1 )
        self.conv2 = nn.Conv2d( 32, 64, 3, padding = 1 )

        self.pool = nn.MaxPool2d( 2, 2 )
        self.fc1 = nn.Linear( 64 * 7 * 7, 128 )
        self.fc2 = nn.Linear( 128, 62 ) #0-9 + a-z + A-Z

    def forward( self, x ) :
        x = F.relu( self.conv1( x ) )
        x = self.pool(x)
        x = F.relu( self.conv2( x ) )
        x = self.pool( x )
        x = torch.flatten( x, 1 )
        x = F.relu( self.fc1( x ) )
        return self.fc2( x )

def calculate_accuracy( loader, model ) :
    correct = 0
    total = 0
    model.eval()
    with torch.no_grad() :
        for Xb, yb in loader :
            preds = model( Xb )
            predicted = torch.argmax( preds, dim = 1 )
            correct += ( predicted == yb ).sum().item()
            total += yb.size( 0 )
    accuracy = 100 * correct / total
    return accuracy

def calculate_loss( loader, model, criterion ) :
    total_loss = 0
    model.eval()
    with torch.no_grad():
        for Xb, yb in loader :
            preds = model( Xb )
            loss = criterion( preds, yb )
            total_loss += loss.item()
    return total_loss / len( loader )


















