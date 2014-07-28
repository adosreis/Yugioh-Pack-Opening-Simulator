#!/usr/bin/perl -w
use strict;
use HTML::TableExtract;
use JSON;

my @country = qw/EN FR DE IT SP PT JP/;
my $country_codes = join '|', @country;

open my $file, '<', $ARGV[0] or die "Cannot open '$ARGV[0]': $!\n";

#Before we parse the HTML, get the header names:
my @headers;
while(<$file>)
{
	if(m{^<thead>} .. m{</thead>})
	{
		if(/"col"> (.*)$/) {push @headers, $1; }
	}
}

#Move back to the beginning of the file:
seek($file, 0, 0);

#Parse the table:
my $te = HTML::TableExtract->new(headers => \@headers);
$te->parse_file($file);
close $file;

#Get the table:
my $set = [ ];
my $filename = undef;
for my $ts($te->tables)
{
	#Every row gives us info on a single card:
	for my $row($ts->rows) 
	{
		#Remove annoying newlines and spaces:
		for(@$row) { chomp $_; s/ // }
		my ($set_id, $name, $rarity, $cat) = @$row;

		#If we haven't got it yet, get the file name (the set and country code):
		if(! defined $filename)
		{
			if($set_id =~ /((?:\w){3,4}-$country_codes)/) { $filename = "jsons/$1.json" }
		}
		#If a card has more than one rarity, split it into an array:
		if($rarity =~/\n/)
		{
			my @rarities = split '\n', $rarity;
			my $rarity = \@rarities;
		}
		push @$set, { set_number => $set_id, name => $name, rarity => $rarity };
	}
}

open $file, ">", $filename or die "Cannot open '$filename': $!\n";
print $file to_json($set, { pretty => 1 });

__END__

=head1 PROGRAM

Reads in a html document, the set card list for a set from the YuGiOh! Wikia,
(for example, I<yugioh.wikia.com/wiki/Set_Card_Lists:Primal_Origin_(TCG-EN).html>)
and generates a JSON document from the table.

=cut

=head1 USAGE

Usage is simple enough, just invoke the program and give the html document in
the command line arguments:

 wget "http://yugioh.wikia.com/wiki/Set_Card_Lists:Primal_Origin_(TCG-EN)" -O prio.html
 ./pack-to-json.pl prio.html

Will generate a file named B<PRIO-EN.json>.

=cut

=head1 AUTHOR

Alex Kerr, C<< <kirbyman62@gmail.com> >>

=cut
