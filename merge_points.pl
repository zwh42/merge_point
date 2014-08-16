use strict;
use Getopt::Long; 
use XML::Simple;
use Data::Dumper;

my @x1 = (8, 10, 2, 8, 6, 0, 2, 4, 7, 1);
my @y1 = (6, 1, 1, 5, 5, 6, 10, 2, 8, 10);
my @x2 = (42, 43, 40, 41, 50, 43, 45, 40, 46, 41);
my @y2 = (43, 47, 41, 47, 43, 43, 42, 42, 41, 46);

print Dumper(@x1), "\n" ;
print Dumper(@y2), "\n" ;


my @point = ();

for(my $i = 0; $i < 10; $i++){
   push(@point, {"x" => $x1[$i], "y" => $y1[$i],"used" => 0});
   push(@point, {"x" => $x2[$i], "y" => $y2[$i],"used" => 0});  
}

print Dumper(@point);
#<STDIN>;

my $threshold = 3;

sub mergeCareArea{
	my $points = $_[0];
	my $threshold = $_[1];
	
	print Dumper($points);
	print "up: points inside function\n";
	#<STDIN>;
	print "threshold = $threshold \n";
	print "start merge ...\n";
	#<STDIN>;
	
	my @boxes = ();
#	for (my $i = 0; $i < scalar(@$points); $i++){
#		#print "merge hotspot: ","x = ",@$points[$i]->{x}, "  y = ", @$points[$i]->{y},  "\n";	
#  	};

  	my $i = 0;

    while ($i < scalar(@$points)) {
    	my $pt1 = @$points[$i];
    	my @table = ();
    	if ($pt1->{used} == 1){
    		$i++;
    		next;
    	}
    	push(@table,$pt1);
        $pt1->{used} = 1;
    	print "table before loop: \n";
    	print Dumper(@table);
    	#<STDIN>;
    	
    	
    	my $j = 0;
    	while ($j < scalar(@$points)){
    		print "real j = " , $j, "\n";
    		my $pt2 = @$points[$j];
    		if ($pt2->{used} == 1){
    			$j++;
    			next;
    		}

    		my $add_to_table = 0;
    		my $k = 0;

    		while ($k < scalar(@table)) {
    		 	my $pt3 = $table[$k];
    		 	if ($pt3 == $pt2){
    		 		$k++;
    		 		print "pt3 == pt2, pass..\n";
    		 		next;
    		 	}
                
                print "pt2 = ", Dumper($pt2), "\n";
                print "pt3 = ", Dumper($pt3), "\n";
                my $distance = (($pt3->{x} - $pt2->{x}) ** 2 + ($pt3->{y} - $pt2->{y}) ** 2) ** 0.5;
                print "distance = $distance \n";
                #<STDIN>;
                if ($distance <= $threshold){
                	print "distance =", $distance,"<", "threshold = ",$threshold , "will be added to table \n";
                	$add_to_table = 1;
                	last;
                }
                $k ++;
    		}

    		if ($add_to_table == 1){
    			print "table before add: \n";
                print Dumper(@table);
    			push(@table, $pt2);
    			$pt2->{used} = 1;
    			print "table after add: \n";
                print Dumper(@table);
                #<STDIN>;
                $add_to_table = 0;
    			$j = 0;
    			print "reset j = " , $j , "\n";
    		}else{
    			$j++;
    		} 
    	}    
        
        push(@boxes, \@table);
    	$i++;	

    }

    
    print "Dumper boxes : \n";
    <STDIN>;

    print Dumper(\@boxes);
    <STDIN>;
    print "boxes size: \n";
    print scalar(@boxes), "\n";

    # for(my $i = 0; $i < $#boxes; $i++){
    #     print "box number ", "$i \n" ;
    #     for (my $j = 0; $j < scalar($boxes[$i]); $j++){
    #         print $boxes[$i][$j], "\n";
    #     }
    #     print "finished";
    # }

    for(my $i = 0; $i < scalar(@boxes);$i++){
        #print "size of $i =", @{$boxes[$i]}, "\n";
        my @table = @{$boxes[$i]};
        my $table_size = scalar(@table);
        # print "table size = ", scalar(@table);
        # print "table element 0 X= ", $table[0]->{x};
        # print "table element 0 Y= ", $table[0]->{y};
        # <STDIN>;
        my $min_x = $table[0]->{x}; 
        my $min_y = $table[0]->{y};
        my $max_x = $table[0]->{x};
        my $max_y = $table[0]->{y}; 
        for(my $j = 1; $j < $table_size; $j++){
            $min_x = $table[$j]->{x} if $table[$j]->{x} < $min_x;
            $min_y = $table[$j]->{y} if $table[$j]->{y} < $min_y;
            $max_x = $table[$j]->{x} if $table[$j]->{x} > $max_x;
            $max_y = $table[$j]->{y} if $table[$j]->{y} > $max_y;   
        }

        print "min x = $min_x, min y = $min_y, max x = $max_x, max y = $max_y \n";

    }




}

mergeCareArea(\@point, $threshold);